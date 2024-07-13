package cn.krain.weibo_data_analysis_web.service;

import cn.krain.weibo_data_analysis_web.entity.SystemArticleComment;
import cn.krain.weibo_data_analysis_web.entity.SystemWeekRank;
import cn.krain.weibo_data_analysis_web.vo.SystemWeekRankVo;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Map;

/**
 * @author cc
 * @data 2022/5/5 - 22:56
 */
@Service
public interface SystemArticleCommentService {
    List<SystemArticleComment> queryCommentEmotion(Map<String, Object> map);

    List<SystemArticleComment> queryCommEmoList(Map<String, Object> map);

    int getTotalByTopicName(Map<String, Object> map);
}
