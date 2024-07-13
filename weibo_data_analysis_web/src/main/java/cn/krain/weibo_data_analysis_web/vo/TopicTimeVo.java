package cn.krain.weibo_data_analysis_web.vo;

import lombok.Data;

/**
 * @author cc
 * @data 2022/5/13 - 23:49
 */
@Data
public class TopicTimeVo {
    private String id;
    private String topic_name;
    private String topic_time;
    private String count;
}
