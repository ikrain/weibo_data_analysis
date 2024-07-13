package cn.krain.weibo_data_analysis_web.dao;

import cn.krain.weibo_data_analysis_web.vo.SystemCommentMapVo;
import cn.krain.weibo_data_analysis_web.vo.SystemTopicAreaVo;

import java.util.List;

/**
 * @author cc
 * @data 2022/5/5 - 22:54
 */
public interface SystemTopicAreaDao {

    List<SystemTopicAreaVo> selectTopicArea();
}
