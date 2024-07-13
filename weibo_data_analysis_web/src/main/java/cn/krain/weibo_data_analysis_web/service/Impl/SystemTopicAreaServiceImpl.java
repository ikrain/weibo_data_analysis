package cn.krain.weibo_data_analysis_web.service.Impl;

import cn.krain.weibo_data_analysis_web.dao.SystemTopicAreaDao;
import cn.krain.weibo_data_analysis_web.service.SystemTopicAreaService;
import cn.krain.weibo_data_analysis_web.vo.SystemTopicAreaVo;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

/**
 * @author cc
 * @data 2022/5/10 - 22:57
 */
@Service
public class SystemTopicAreaServiceImpl implements SystemTopicAreaService {

    @Autowired
    SystemTopicAreaDao systemTopicAreaDao;

    @Override
    public List<SystemTopicAreaVo> queryTopicAreaVo() {
        return systemTopicAreaDao.selectTopicArea();
    }
}
