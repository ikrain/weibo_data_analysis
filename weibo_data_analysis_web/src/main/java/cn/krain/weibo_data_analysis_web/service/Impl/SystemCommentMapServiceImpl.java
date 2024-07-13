package cn.krain.weibo_data_analysis_web.service.Impl;

import cn.krain.weibo_data_analysis_web.dao.SystemCommentMapDao;
import cn.krain.weibo_data_analysis_web.entity.SystemCommentMap;
import cn.krain.weibo_data_analysis_web.service.SystemCommentMapService;
import cn.krain.weibo_data_analysis_web.vo.SystemCommentMapVo;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

/**
 * @author cc
 * @data 2022/5/10 - 18:57
 */
@Service
public class SystemCommentMapServiceImpl implements SystemCommentMapService {

    @Autowired
    SystemCommentMapDao systemCommentMapDao;

    @Override
    public List<SystemCommentMapVo> queryCommentMap() {
        return systemCommentMapDao.selectCommentMap();
    }
}
