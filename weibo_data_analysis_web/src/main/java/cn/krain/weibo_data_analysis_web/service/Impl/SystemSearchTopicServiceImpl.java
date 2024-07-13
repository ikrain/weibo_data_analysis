package cn.krain.weibo_data_analysis_web.service.Impl;

import cn.krain.weibo_data_analysis_web.dao.SystemSearchTopicDao;
import cn.krain.weibo_data_analysis_web.service.SystemSearchTopicService;
import cn.krain.weibo_data_analysis_web.vo.SystemSearchTopicVo;
import cn.krain.weibo_data_analysis_web.vo.SystemWeekRankVo;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Map;

/**
 * @author cc
 * @data 2022/5/12 - 17:23
 */
@Service
public class SystemSearchTopicServiceImpl implements SystemSearchTopicService {

    @Autowired
    private  SystemSearchTopicDao systemSearchTopicDao;

    @Override
    public List<SystemSearchTopicVo> querySearchTopic(Map<String, Object> map) {
        return systemSearchTopicDao.selectSearchTopic(map);
    }

    @Override
    public int getTotalByContent(Map<String, Object> map) {
        return systemSearchTopicDao.countTotalByContent(map);
    }
}
