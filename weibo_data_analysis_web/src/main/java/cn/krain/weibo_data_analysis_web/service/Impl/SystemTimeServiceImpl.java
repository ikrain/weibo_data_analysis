package cn.krain.weibo_data_analysis_web.service.Impl;

import cn.krain.weibo_data_analysis_web.dao.SystemTimeDao;
import cn.krain.weibo_data_analysis_web.service.SystemTimeService;
import cn.krain.weibo_data_analysis_web.vo.ArticleTimeVo;
import cn.krain.weibo_data_analysis_web.vo.CommentTimeVo;
import cn.krain.weibo_data_analysis_web.vo.TopicTimeVo;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

/**
 * @author cc
 * @data 2022/5/13 - 23:57
 */
@Service
public class SystemTimeServiceImpl implements SystemTimeService {

    @Autowired
    private SystemTimeDao systemTimeDao;

    @Override
    public List<TopicTimeVo> queryTopicTime() {
        return systemTimeDao.selectTopicTime();
    }

    @Override
    public List<ArticleTimeVo> queryArticleTime() {
        return systemTimeDao.selectArticleTime();
    }

    @Override
    public List<CommentTimeVo> queryCommentTime() {
        return systemTimeDao.selectCommentTime();
    }

    @Override
    public int queryTopicNum() {
        return systemTimeDao.selectTopicNum();
    }

    @Override
    public int queryArticleNum() {
        return systemTimeDao.selectArticleNum();
    }

    @Override
    public int queryArticleAddNum() {
        return systemTimeDao.selectArticleAddNum();
    }

    @Override
    public int queryTopicAddNum() {
        return systemTimeDao.selectTopicAddNum();
    }
}
