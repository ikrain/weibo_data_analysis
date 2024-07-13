package cn.krain.weibo_data_analysis_web.vo;

import lombok.Data;

/**
 * @author cc
 * @data 2022/5/10 - 21:11
 */
@Data
public class SystemSearchTopicVo {
    private String article_id;
    private String author_name;
    private String article_content;
    private String article_time;
    private String article_emotion;
    private String emotion_state;
    private String article_hot_value;
    private String article_link;
}
