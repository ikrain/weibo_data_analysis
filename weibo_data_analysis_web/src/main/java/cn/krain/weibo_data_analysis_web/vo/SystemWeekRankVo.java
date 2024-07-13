package cn.krain.weibo_data_analysis_web.vo;

import lombok.Data;

/**
 * @author cc
 * @data 2022/5/10 - 21:11
 */
@Data
public class SystemWeekRankVo {
    private String id;
    private String topic_name;
    private String topic_num;
    private String topic_time;
    private String topic_category;
    private String topic_introduction;
    private String topic_host;
    private String topic_read_num;
    private String topic_talk_num;
    private String topic_original_num;
    private String topic_read_trend;
    private String topic_talk_trend;
    private String topic_original_trend;
}
