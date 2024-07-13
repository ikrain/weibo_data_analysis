package cn.krain.weibo_data_analysis_web.result;

/**
 * @author cc
 * @data 2022/5/6 - 9:25
 */

import lombok.Data;

@Data
public class ResultVo<T> {

    /**
     * 请求状态码
     */
    private Integer code;

    /**
     * 提示信息
     */
    private String message;

    /**
     * 响应数据
     */
    private T data;

    /**
     * 标志请求成功与否
     */
    private boolean success;
}
