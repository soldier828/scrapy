#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 13:03:44 2017

@author: liunan
"""

from python_zhihu import ZhiHu

zh=ZhiHu()


#zh.get_answer_text('https://www.zhihu.com/question/55482205')
zh.get_question_followers('https://www.zhihu.com/question/22591304/followers')