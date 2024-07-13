package cn.krain.weibo_data_analysis_web.dao;

import cn.krain.weibo_data_analysis_web.entity.SystemUser;
import cn.krain.weibo_data_analysis_web.vo.ArticleTimeVo;
import cn.krain.weibo_data_analysis_web.vo.CommentTimeVo;
import cn.krain.weibo_data_analysis_web.vo.SystemUserVo;
import cn.krain.weibo_data_analysis_web.vo.TopicTimeVo;

import java.util.List;
import java.util.Map;

/**
 * @author cc
 * @data 2022/5/5 - 22:54
 */
public interface SystemTimeDao {

    List<TopicTimeVo> selectTopicTime();

    List<ArticleTimeVo> selectArticleTime();

    List<CommentTimeVo> selectCommentTime();

    int selectTopicNum();

    int selectArticleNum();

    int selectArticleAddNum();

    int selectTopicAddNum();
}
