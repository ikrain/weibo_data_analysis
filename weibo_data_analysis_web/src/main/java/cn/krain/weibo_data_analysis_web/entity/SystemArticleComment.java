package cn.krain.weibo_data_analysis_web.entity;

import lombok.Data;

/**
 * @author cc
 * @data 2022/5/11 - 10:08
 */
@Data
public class SystemArticleComment {
    private String id;
    private String topic_id;
    private String topic_name;
    private String article_id;
    private String comment_time;
    private String comment_content;
    private String comment_author_name;
    private String comment_emotion;
    private String emotion_state;
}
