import yfinance as yf
import numpy as np
import scipy.optimize as sc
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px
from scipy.stats import norm
from scipy.optimize import minimize
import time
import warnings
import os

# Functional Paradigm: Data downloading with retry mechanism
def download_data(tickers, start_date, end_date, retries=3, delay=5):
    for _ in range(retries):
        try:
            data = yf.download(tickers=tickers, start=start_date, end=end_date)
            if not data['Adj Close'].empty:
                return data['Adj Close']
        except Exception as e:
            print(f"Download failed: {e}. Retrying in {delay} seconds...")
            time.sleep(delay)
    print("Failed to download data. Switching to Excel backup...")
    return None
class PortfolioOptimizer:
    def __init__(
            self, stocks, start, end, excel_file, UserReturn, riskFreeRate=0.044):
        self.stocks =stocks
        self.start =start
        self.end =end
        self.excel_file = excel_file
        self.UserReturn =UserReturn
        self.riskFreeRate = riskFreeRate
        self.prices = self.basicMetrics()
        self.returns = np.log(self.prices / self.prices.shift(1)).dropna()
        self.pBar = self.returns.mean()
        self.Sigma = self.returns.cov()
        self.weights = np.array([0.1] * len(self.prices.columns))
        self.meanReturns, self.covMatrix = self.getData()
        
        self.optimized_allocation=self.allocation()

    def basicMetrics(self):
        prices = download_data(self.stocks, self.start, self.end)
        if prices is None:
            current_dir = os.path.dirname(__file__)
            excel_path = os.path.join(current_dir, self.excel_file)
            prices = pd.read_excel(excel_path, index_col=0, parse_dates=True)
        return prices
             

   

    def getData(self):
        returns = self.basicMetrics()
        meanReturns = (returns.mean())  
        covMatrix = (returns.cov())  
        return meanReturns, covMatrix

    def calculate_metrics(self):
        port_variance = self.portfolio_variance(self.weights, self.Sigma)
        port_annual_ret = np.sum(self.pBar * self.weights)
        port_volatility = np.sqrt(port_variance)
        sharpe_ratio = (port_annual_ret - self.risk_free_rate) / port_volatility
        return port_annual_ret, port_volatility, port_variance, sharpe_ratio

    def portfolio_variance(self, weights, Sigma):
        return np.dot(weights.T, np.dot(Sigma, weights))    

    
    def portfolioReturn(self, weights):  
        return np.sum(self.pBar * weights)

    def portfolioPerformance(self, weights):
        port_annual_ret = np.sum(self.meanReturns * weights)
        port_variance = self.portfolio_variance(weights, self.Sigma)
        port_volatility = np.sqrt(port_variance)
        return port_annual_ret, port_volatility

    def riskFunction(self, w):
        return self.portfolio_variance(w, self.Sigma)

    def singleEquationSolver(self):
        Sigma_inv = np.linalg.inv(self.Sigma)
        sum_all_elements = np.sum(Sigma_inv)
        w_opt = np.sum(Sigma_inv, axis=1) / sum_all_elements
        w_opt = np.maximum(w_opt, 0) / np.sum(np.maximum(w_opt, 0))
        return w_opt

    def markowitz_optimal_weights_specific_return(self, UserReturn):
        Sigma_inv = np.linalg.inv(self.Sigma)
        M = np.dot(np.dot(self.pBar.T, Sigma_inv), self.pBar)
        w_opt = np.dot(Sigma_inv, self.pBar) * (UserReturn / M)
        w_opt = np.maximum(w_opt, 0)
        return w_opt
    def allocation(self):
        optimized_allocation = pd.DataFrame(
            self.singleEquationSolver(),
            index=self.meanReturns.index,
            columns=["allocation"],
        )
        return optimized_allocation