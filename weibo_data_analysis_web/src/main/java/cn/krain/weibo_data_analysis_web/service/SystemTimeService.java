package cn.krain.weibo_data_analysis_web.service;

import cn.krain.weibo_data_analysis_web.vo.ArticleTimeVo;
import cn.krain.weibo_data_analysis_web.vo.CommentTimeVo;
import cn.krain.weibo_data_analysis_web.vo.SystemCommentMapVo;
import cn.krain.weibo_data_analysis_web.vo.TopicTimeVo;
import org.springframework.stereotype.Service;

import java.util.List;

/**
 * @author cc
 * @data 2022/5/5 - 22:56
 */
@Service
public interface SystemTimeService {

    List<TopicTimeVo> queryTopicTime();

    List<ArticleTimeVo> queryArticleTime();

    List<CommentTimeVo> queryCommentTime();

    int queryTopicNum();

    int queryArticleNum();

    int queryArticleAddNum();

    int queryTopicAddNum();
}
