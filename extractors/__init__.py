# -*- coding: utf-8 -*-
"""
Created on Thu Dec 18 10:45:54 2025

@author: C
"""

from .udn import extract as extract_udn
from .ltn import extract as extract_ltn
from .yahoo import extract as extract_yahoo
from .money_udn import extract as extract_money_udn
from .chinatimes import extract as extract_chinatimes
from .ctee import extract as extract_ctee
from .cnyes import extract as extract_cnyes
from .ettoday import extract as extract_ettoday
from .ebc import extract as extract_ebc
from .cmoney import extract as extract_cmoney
from .moneyweekly import extract as extract_moneyweekly
from .money_link import extract as extract_money_link
from .ftnn import extract as extract_ftnn
from .cmnews import extract as extract_cmnews
from .businesstoday import extract as extract_businesstoday
from .wantrich import extract as extract_wantrich
from .moneydj import extract as extract_moneydj
from .nvns import extract as extract_nvns
from .businessweekly import extract as extract_businessweekly
from .msn import extract as extract_msn
from .focus import extract as extract_focus
from .bo6s import extract as extract_bo6s
from .nownews import extract as extract_nownews
from .line import extract as extract_line
from .aastocks import extract as extract_aastock
from .reccessary import extract as extract_reccessary

DOMAIN_EXTRACTORS = {
    'udn.com': extract_udn,
    'ec.ltn.com.tw': extract_ltn,
    'tw.stock.yahoo.com': extract_yahoo,
    'tw.news.yahoo.com': extract_yahoo,
    'money.udn.com': extract_money_udn,
    'www.chinatimes.com':extract_chinatimes,
    'www.ctee.com.tw':extract_ctee,
    'news.cnyes.com':extract_cnyes,
    'finance.ettoday.net':extract_ettoday,
    'fnc.ebc.net.tw':extract_ebc,
    'www.cmoney.tw':extract_cmoney,
    'cmnews.com.tw':extract_cmnews,
    'www.moneyweekly.com.tw':extract_moneyweekly,
    'ww2.money-link.com.tw':extract_money_link,
    'www.ftnn.com.tw':extract_ftnn,
    'www.businesstoday.com.tw':extract_businesstoday,
    'wantrich.chinatimes.com':extract_wantrich,
    'www.moneydj.com':extract_moneydj,
    'nvns.net':extract_nvns,
    'wealth.businessweekly.com.tw':extract_businessweekly,
    'www.msn.com':extract_msn,
    'focus.586.com.tw':extract_focus,
    'www.bo6s.com.tw':extract_bo6s,
    'www.nownews.com':extract_nownews,
    'today.line.me':extract_line,
    'www.aastocks.com':extract_aastock,
    'www.reccessary.com':extract_reccessary,
}