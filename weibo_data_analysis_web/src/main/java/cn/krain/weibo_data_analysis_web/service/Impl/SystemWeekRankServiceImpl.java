package cn.krain.weibo_data_analysis_web.service.Impl;

import cn.krain.weibo_data_analysis_web.dao.SystemWeekRankDao;
import cn.krain.weibo_data_analysis_web.entity.SystemWeekRank;
import cn.krain.weibo_data_analysis_web.service.SystemWeekRankService;
import cn.krain.weibo_data_analysis_web.vo.SystemWeekRankVo;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Map;

/**
 * @author cc
 * @data 2022/5/11 - 10:25
 */
@Service
public class SystemWeekRankServiceImpl implements SystemWeekRankService {

    @Autowired
    private SystemWeekRankDao systemWeekRankDao;

    @Override
    public List<SystemWeekRankVo> queryWeekRank(Map<String, Object> map) {
        return systemWeekRankDao.selectWeekRank(map);
    }

    @Override
    public int getTotalByContent(Map<String, Object> map) {
        return systemWeekRankDao.countTotalByContent(map);
    }

    @Override
    public List<SystemWeekRank> queryNewTopic() {
        return systemWeekRankDao.selectNewTopic();
    }

    @Override
    public List<SystemWeekRank> getTopicByWord(String senWord) {
        return systemWeekRankDao.selectTopicByWord(senWord);
    }

    @Override
    public List<SystemWeekRank> getNumByWord(String title) {
        return systemWeekRankDao.selectNumByWord(title);
    }
}
