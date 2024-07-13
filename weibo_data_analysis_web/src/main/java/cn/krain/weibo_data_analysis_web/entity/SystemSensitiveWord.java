package cn.krain.weibo_data_analysis_web.entity;

import lombok.Data;

/**
 * @author cc
 * @data 2022/5/11 - 10:08
 */
@Data
public class SystemSensitiveWord {
    private String id;
    private String sensitive_word;
    private String create_time;
    private String creater;
}
