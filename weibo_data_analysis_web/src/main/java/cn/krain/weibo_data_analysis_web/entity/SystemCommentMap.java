package cn.krain.weibo_data_analysis_web.entity;

import lombok.Data;

import java.io.Serializable;

/**
 * @author cc
 * @data 2022/5/10 - 18:50
 */
@Data
public class SystemCommentMap implements Serializable {
    private String id;
    private String province;
    private String comment_num;
}
