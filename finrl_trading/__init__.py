"""FinRL-Trading: Reinforcement Learning for Quantitative Trading.

This package provides tools and utilities for building, training, and
deploying reinforcement learning agents for financial trading.

Modules:
    config: Configuration management and constants
    data: Data downloading, preprocessing, and feature engineering
    env: Trading environment implementations (OpenAI Gym compatible)
    agents: RL agent wrappers (PPO, A2C, DDPG, SAC, TD3)
    models: Model training and evaluation utilities
    portfolio: Portfolio optimization and risk management
    backtest: Backtesting engine and performance metrics

Notes:
    Personal fork for learning purposes. Main areas of interest:
    - Experimenting with custom reward shaping in the trading env
    - Testing SAC and TD3 agents on crypto market data
"""

__version__ = "0.1.0"
__author__ = "FinRL-Trading Contributors"
__license__ = "MIT"

from finrl_trading import config

__all__ = [
    "config",
    "__version__",
    "__author__",
    "__license__",
]
