from pydantic import BaseModel
from typing import List, Optional


class Location(BaseModel):
    country: str
    city: Optional[str] = None


class Skills(BaseModel):
    technical: List[str]
    soft: List[str]
    languages: List[str]


class Interests(BaseModel):
    industries: List[str]
    roles: Optional[List[str]] = None
    workStyle: Optional[str] = None  # "remote" | "onsite" | "hybrid" | "no_preference"
    relocation: Optional[str] = None  # "no" | "within_country" | "within_mena" | "global"


class Constraints(BaseModel):
    internetAccess: Optional[str] = None  # "low" | "medium" | "good"
    canPayForCourses: Optional[bool] = None
    timePerWeekHours: Optional[int] = None
    other: Optional[str] = None


class UserProfile(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    location: Location
    educationLevel: str
    educationField: Optional[str] = None
    currentStatus: str  # "student" | "job_seeker" | "employed" | "career_switcher"
    experienceYears: Optional[float] = None
    currentRole: Optional[str] = None
    skills: Skills
    interests: Interests
    constraints: Optional[Constraints] = None


class SuggestedRole(BaseModel):
    title: str
    description: str
    whyFitForUser: str
    menaDemandContext: str


class SkillGapAnalysis(BaseModel):
    strengths: List[str]
    gaps: List[str]
    prioritySkillsToBuild: List[str]


class LearningPlanStep(BaseModel):
    month: int
    focus: str
    actions: List[str]
    suggestedResources: List[str]


class LearningPlan(BaseModel):
    horizonMonths: int
    stepsByMonth: List[LearningPlanStep]


class JobSearchStrategy(BaseModel):
    platforms: List[str]
    networkingTips: List[str]
    applicationTips: List[str]


class CareerInsightsResponse(BaseModel):
    profileSnapshot: str
    suggestedRoles: List[SuggestedRole]
    skillGapAnalysis: SkillGapAnalysis
    learningPlan: LearningPlan
    jobSearchStrategy: JobSearchStrategy
    constraintsNotes: Optional[str] = None