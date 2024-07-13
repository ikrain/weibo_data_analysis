package cn.krain.weibo_data_analysis_web.result.Enum;

import lombok.Getter;

/**
 * @author cc
 * @data 2022/5/6 - 9:18
 */
@Getter
public enum ResultEnum {

    SUCCESS(200, "成功"),

    ERROR(500, "错误");

    private Integer code;
    private String message;

    ResultEnum(Integer code, String message) {
        this.code = code;
        this.message = message;
    }
}
