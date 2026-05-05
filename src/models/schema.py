from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any


# ---------------------------
# Request Schema
# ---------------------------
class PortfolioItem(BaseModel):
    ticker: str
    value: float


class QueryRequest(BaseModel):
    query: str
    session_id: Optional[str] = "default"
    portfolio: Optional[List[PortfolioItem]] = []


# ---------------------------
# Safety Schema
# ---------------------------
class SafetyResponse(BaseModel):
    blocked: bool
    reason: Optional[str] = None
    message: Optional[str] = None


# ---------------------------
# Classifier Schema
# ---------------------------
class Entities(BaseModel):
    tickers: List[str] = []
    amount: Optional[float] = None
    period_years: Optional[float] = None


class ClassificationOutput(BaseModel):
    intent: str
    agent: str
    entities: Entities
    safety_verdict: str


# ---------------------------
# Portfolio Agent Schema
# ---------------------------
class ConcentrationRisk(BaseModel):
    top_position_pct: float
    top_3_positions_pct: float
    flag: str  # low | moderate | high


class Performance(BaseModel):
    total_return_pct: float
    annualized_return_pct: float


class BenchmarkComparison(BaseModel):
    benchmark: str
    portfolio_return_pct: float
    benchmark_return_pct: float
    alpha_pct: float


class Observation(BaseModel):
    severity: str  # info | warning
    text: str


class PortfolioResponse(BaseModel):
    concentration_risk: Optional[ConcentrationRisk] = None
    performance: Optional[Performance] = None
    benchmark_comparison: Optional[BenchmarkComparison] = None
    observations: List[Observation]
    disclaimer: str


# ---------------------------
# Stub Agent Schema
# ---------------------------
class StubResponse(BaseModel):
    agent: str
    intent: str
    entities: Dict[str, Any]
    message: str


# ---------------------------
# SSE Event Schema (Optional but strong design)
# ---------------------------
class SSEEvent(BaseModel):
    event: str
    data: Any