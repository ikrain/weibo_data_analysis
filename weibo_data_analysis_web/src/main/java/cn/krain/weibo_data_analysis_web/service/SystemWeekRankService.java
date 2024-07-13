package cn.krain.weibo_data_analysis_web.service;

import cn.krain.weibo_data_analysis_web.entity.SystemWeekRank;
import cn.krain.weibo_data_analysis_web.vo.SystemCommentMapVo;
import cn.krain.weibo_data_analysis_web.vo.SystemWeekRankVo;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Map;

/**
 * @author cc
 * @data 2022/5/5 - 22:56
 */
@Service
public interface SystemWeekRankService {
    List<SystemWeekRankVo> queryWeekRank(Map<String, Object> map);

    int getTotalByContent(Map<String, Object> map);

    List<SystemWeekRank> queryNewTopic();

    List<SystemWeekRank> getTopicByWord(String senWord);

    List<SystemWeekRank> getNumByWord(String title);
}
