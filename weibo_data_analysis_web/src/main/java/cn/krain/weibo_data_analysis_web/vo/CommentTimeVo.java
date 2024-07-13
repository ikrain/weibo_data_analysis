package cn.krain.weibo_data_analysis_web.vo;

import lombok.Data;

/**
 * @author cc
 * @data 2022/5/13 - 23:49
 */
@Data
public class CommentTimeVo {
    private String id;
    private String topic_id;
    private String article_id;
    private String comment_time;
    private String count;
}
