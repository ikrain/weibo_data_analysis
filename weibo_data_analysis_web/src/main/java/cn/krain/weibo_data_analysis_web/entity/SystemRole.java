package cn.krain.weibo_data_analysis_web.entity;

import lombok.Data;

import java.io.Serializable;

/**
 * @author cc
 * @data 2022/5/5 - 22:55
 */
@Data
public class SystemRole implements Serializable {
    private String id;
    private String role_name;
    private String menu;
    private String represent;
}
