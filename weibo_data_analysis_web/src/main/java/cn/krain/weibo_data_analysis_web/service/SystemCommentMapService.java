package cn.krain.weibo_data_analysis_web.service;

import cn.krain.weibo_data_analysis_web.entity.SystemCommentMap;
import cn.krain.weibo_data_analysis_web.entity.SystemUser;
import cn.krain.weibo_data_analysis_web.vo.SystemCommentMapVo;
import cn.krain.weibo_data_analysis_web.vo.SystemUserVo;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Map;

/**
 * @author cc
 * @data 2022/5/5 - 22:56
 */
@Service
public interface SystemCommentMapService {
    List<SystemCommentMapVo> queryCommentMap();
}
