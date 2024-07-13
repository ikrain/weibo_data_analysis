package cn.krain.weibo_data_analysis_web.vo;

import lombok.Data;

import java.io.Serializable;

/**
 * @author cc
 * @data 2022/5/9 - 23:03
 */
@Data
public class SystemUserVo implements Serializable {
    private String id;
    private String username;
    private String password;
    private String role_id;
    private String token;
    private String role_name;
    private String avatar;
    private String create_time;
    private String role_menu;
    private String role_represent;
}
