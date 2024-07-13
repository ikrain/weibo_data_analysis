package cn.krain.weibo_data_analysis_web.dao;

import cn.krain.weibo_data_analysis_web.entity.SystemCommentMap;
import cn.krain.weibo_data_analysis_web.entity.SystemUser;
import cn.krain.weibo_data_analysis_web.vo.SystemCommentMapVo;
import cn.krain.weibo_data_analysis_web.vo.SystemUserVo;

import java.util.List;
import java.util.Map;

/**
 * @author cc
 * @data 2022/5/5 - 22:54
 */
public interface SystemCommentMapDao {

    List<SystemCommentMapVo> selectCommentMap();
}
