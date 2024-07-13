package cn.krain.weibo_data_analysis_web.dao;

import cn.krain.weibo_data_analysis_web.entity.SystemWeekRank;
import cn.krain.weibo_data_analysis_web.vo.SystemCommentMapVo;
import cn.krain.weibo_data_analysis_web.vo.SystemWeekRankVo;

import java.util.List;
import java.util.Map;

/**
 * @author cc
 * @data 2022/5/5 - 22:54
 */
public interface SystemWeekRankDao {
    List<SystemWeekRankVo> selectWeekRank(Map<String, Object> map);

    int countTotalByContent(Map<String, Object> map);

    List<SystemWeekRank> selectNewTopic();

    List<SystemWeekRank> selectTopicByWord(String senWord);

    List<SystemWeekRank> selectNumByWord(String title);
}
