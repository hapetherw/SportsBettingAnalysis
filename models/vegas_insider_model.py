import datetime
from sqlalchemy import Column, Integer, String, DateTime

from models.model import Base


class VegasInsider(Base):
    __tablename__ = 'VegasInsider'
    ID = Column(Integer, primary_key=True, autoincrement=True)
    TeamName = Column(String, nullable=True)
    Rank = Column(String, nullable=True)
    TOTAL_POWER = Column(String, nullable=True)
    CONF_ADJ_PERF_NDEX = Column(String, nullable=True)
    RAW_PERF_NDEX = Column(String, nullable=True)
    CONF_ADJ_RTG = Column(String, nullable=True)
    PURE_RTG = Column(String, nullable=True)
    SU_W = Column(String, nullable=True)
    SU_L = Column(String, nullable=True)
    AVE_PF = Column(String, nullable=True)
    AVE_PA = Column(String, nullable=True)
    AVE_MGN = Column(String, nullable=True)
    PS_W = Column(String, nullable=True)
    PS_L = Column(String, nullable=True)
    PS_P = Column(String, nullable=True)
    HCV = Column(String, nullable=True)
    PURE_AOPR = Column(String, nullable=True)
    CONF_ADJ_AOPR = Column(String, nullable=True)
    ALPA = Column(String, nullable=True)
    ARVL = Column(String, nullable=True)
    SKED_STRGTH = Column(String, nullable=True)
    SKED_STRGTH_CONF_COMP = Column(String, nullable=True)
    RN_W = Column(String, nullable=True)
    RN_L = Column(String, nullable=True)
    createdDate = Column(DateTime, default=datetime.datetime.now())

    def __init__(self, team_name='', rank='', total_power='', conf_adj_perf_ndex='', raw_perf_ndex='', conf_adj_rtg='',
                 pure_rtg='', su_w='', su_l='', ave_pf='', ave_pa='', ave_mgn='', ps_w='', ps_l='', ps_p='', hcv='',
                 pure_aopr='', conf_adj_aopr='', alpa='', arvl='', sked_strgth='', sked_strgth_conf_comp='', rn_w='',
                 rn_l=''):
        self.TeamName = team_name
        self.Rank = rank
        self.TOTAL_POWER = total_power
        self.CONF_ADJ_PERF_NDEX = conf_adj_perf_ndex
        self.RAW_PERF_NDEX = raw_perf_ndex
        self.CONF_ADJ_RTG = conf_adj_rtg
        self.PURE_RTG = pure_rtg
        self.SU_W = su_w
        self.SU_L = su_l
        self.AVE_PF = ave_pf
        self.AVE_PA = ave_pa
        self.AVE_MGN = ave_mgn
        self.PS_W = ps_w
        self.PS_L = ps_l
        self.PS_P = ps_p
        self.HCV = hcv
        self.PURE_AOPR = pure_aopr
        self.CONF_ADJ_AOPR = conf_adj_aopr
        self.ALPA = alpa
        self.ARVL = arvl
        self.SKED_STRGTH = sked_strgth
        self.SKED_STRGTH_CONF_COMP = sked_strgth_conf_comp
        self.RN_W = rn_w
        self.RN_L = rn_l

    def __repr__(self):
        return "<VegasInsider(TeamName='{}', Rank='{}', TOTAL_POWER='{}', CONF_ADJ_PERF_NDEX={}, " \
               "RAW_PERF_NDEX={}, CONF_ADJ_RTG={}, PURE_RTG={}, SU_W={}, SU_L={}, AVE_PF={}, AVE_PA={}, AVE_MGN={}, " \
                "PS_W={}, PS_L={}, PS_P={}, HCV={}, PURE_AOPR={}, CONF_ADJ_AOPR={}, ALPA={}, ARVL={}, SKED_STRGTH={}, "\
                "SKED_STRGTH_CONF_COMP={}, RN_W={}, RN_L={}, createdDate={})>" \
            .format(self.TeamName, self.Rank, self.TOTAL_POWER, self.CONF_ADJ_PERF_NDEX, self.RAW_PERF_NDEX,
                    self.CONF_ADJ_RTG, self.PURE_RTG, self.SU_W, self.SU_L, self.AVE_PF, self.AVE_PA,
                    self.AVE_MGN, self.PS_W, self.PS_L, self.PS_P, self.HCV, self.PURE_AOPR, self.CONF_ADJ_AOPR,
                    self.ALPA, self.ARVL, self.SKED_STRGTH, self.SKED_STRGTH_CONF_COMP, self.RN_W, self.RN_L,
                    self.createdDate)
