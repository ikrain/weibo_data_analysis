package cn.krain.weibo_data_analysis_web.dao;

import cn.krain.weibo_data_analysis_web.entity.SystemArticleComment;
import cn.krain.weibo_data_analysis_web.entity.SystemWeekRank;
import cn.krain.weibo_data_analysis_web.vo.SystemWeekRankVo;

import java.util.List;
import java.util.Map;

/**
 * @author cc
 * @data 2022/5/5 - 22:54
 */
public interface SystemArticleCommentDao {
    List<SystemArticleComment> selectCommentEmotion(Map<String, Object> map);

    List<SystemArticleComment> selectCommEmoList(Map<String, Object> map);

    int countTotalByTN(Map<String, Object> map);
}
