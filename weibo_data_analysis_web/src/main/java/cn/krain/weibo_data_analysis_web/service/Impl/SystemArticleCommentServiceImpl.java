package cn.krain.weibo_data_analysis_web.service.Impl;

import cn.krain.weibo_data_analysis_web.dao.SystemArticleCommentDao;
import cn.krain.weibo_data_analysis_web.entity.SystemArticleComment;
import cn.krain.weibo_data_analysis_web.service.SystemArticleCommentService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Map;

/**
 * @author cc
 * @data 2022/5/13 - 0:17
 */
@Service
public class SystemArticleCommentServiceImpl implements SystemArticleCommentService {

    @Autowired
    private SystemArticleCommentDao systemArticleCommentDao;

    @Override
    public List<SystemArticleComment> queryCommentEmotion(Map<String, Object> map) {
        return systemArticleCommentDao.selectCommentEmotion(map);
    }

    @Override
    public List<SystemArticleComment> queryCommEmoList(Map<String, Object> map) {
        return systemArticleCommentDao.selectCommEmoList(map);
    }

    @Override
    public int getTotalByTopicName(Map<String, Object> map) {
        return systemArticleCommentDao.countTotalByTN(map);
    }
}
