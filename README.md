
<div align="center">

# FinRL-X

### An AI-Native Modular Infrastructure for Quantitative Trading

<img src="https://github.com/user-attachments/assets/80fe89bb-fb09-4267-b29a-76030512f8cf" width="420">

[![Paper](https://img.shields.io/badge/Paper-arXiv_2603.21330-b31b1b?style=for-the-badge)](https://arxiv.org/abs/2603.21330)
&nbsp;
[![PyPI](https://img.shields.io/badge/PyPI-finrl--trading-3775A9?style=for-the-badge&logo=pypi&logoColor=white)](https://pypi.org/project/finrl-trading/)

[![Python 3.11](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
![License](https://img.shields.io/github/license/AI4Finance-Foundation/FinRL-Trading.svg?color=brightgreen)
[![Downloads](https://static.pepy.tech/badge/finrl-trading)](https://pepy.tech/project/finrl-trading)
[![Downloads](https://static.pepy.tech/badge/finrl-trading/week)](https://pepy.tech/project/finrl-trading)
[![Join Discord](https://img.shields.io/badge/Discord-Join-5865F2?logo=discord&logoColor=white)](https://discord.gg/trsr8SXpW5)

![](https://img.shields.io/github/issues-raw/AI4Finance-Foundation/FinRL-Trading?label=Issues)
![](https://img.shields.io/github/issues-pr-raw/AI4Finance-Foundation/FinRL-Trading?label=PRs)
![Visitors](https://api.visitorbadge.io/api/VisitorHit?user=AI4Finance-Foundation&repo=FinRL-Trading&countColor=%23B17A)

*A deployment-consistent trading system that unifies data processing, strategy composition, backtesting, and broker execution through a weight-centric interface.*

[Paper](https://arxiv.org/abs/2603.21330) | [Quick Start](#quick-start) | [Strategies](#strategies) | [Results](#results) | [Discord](https://discord.gg/trsr8SXpW5)

</div>

---

> **Personal fork note:** I'm using this primarily to experiment with the portfolio allocation module ($\mathcal{A}$) and test custom risk overlays. Main upstream repo is at [AI4Finance-Foundation/FinRL-Trading](https://github.com/AI4Finance-Foundation/FinRL-Trading).
>
> **My focus areas:**
> - Custom risk overlays with max drawdown constraints (target: <15% MDD)
> - Comparing equal-weight vs. mean-variance allocation baselines
> - Backtesting on a universe of ~50 large-cap US equities (2018–2024)
>
> **Personal notes / findings so far:**
> - Mean-variance allocation tends to over-concentrate in low-vol names during 2022 drawdown; adding an MDD cap of 12% helped significantly
> - Equal-weight baseline is surprisingly competitive on Sharpe over the full 2018–2024 window — worth keeping as a benchmark
> - TODO: try risk parity weighting as a third baseline

## About

**FinRL-X** is a next-generation, **AI-native** quantitative trading infrastructure that redefines how researchers and practitioners build, test, and deploy algorithmic trading strategies. 

Introduced in our paper *"FinRL-X: An AI-Native Modular Infrastructure for Quantitative Trading"* ([arXiv:2603.21330](https://arxiv.org/abs/2603.21330)), FinRL-X succeeds the original [FinRL](https://github.com/AI4Finance-Foundation/FinRL) framework with a fully modernized architecture designed for the LLM and agentic AI era.

> FinRL-X is **not just a library** — it is a full-stack trading platform engineered around modularity, reproducibility, and production-readiness, supporting everything from ML-based stock selection and professional backtesting to live brokerage execution.

At its cor