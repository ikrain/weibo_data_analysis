package cn.krain.weibo_data_analysis_web.service;

import cn.krain.weibo_data_analysis_web.vo.SystemCommentMapVo;
import cn.krain.weibo_data_analysis_web.vo.SystemTopicAreaVo;
import org.springframework.stereotype.Service;

import java.util.List;

/**
 * @author cc
 * @data 2022/5/5 - 22:56
 */
@Service
public interface SystemTopicAreaService {
    List<SystemTopicAreaVo> queryTopicAreaVo();
}
