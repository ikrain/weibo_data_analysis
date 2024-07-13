package cn.krain.weibo_data_analysis_web.result;

import cn.krain.weibo_data_analysis_web.result.Enum.ResultEnum;

/**
 * @author cc
 * @data 2022/5/6 - 9:26
 */
public class ResultUtil {

    /**
     * 响应请求成功数据实体，包含返回数据
     * @param msg
     * @param objectData
     * @param flag
     * @return
     */
    public static ResultVo success(String msg, Object objectData, boolean flag){
        ResultVo<Object> resultVo = new ResultVo<>();
        resultVo.setCode(ResultEnum.SUCCESS.getCode());
        resultVo.setMessage(msg);
        resultVo.setData(objectData);
        resultVo.setSuccess(flag);
        return resultVo;
    }

    /**
     * 响应请求成功数据实体（不含返回数据）
     * @param msg
     * @param flag
     * @return
     */
    public static ResultVo success(String msg, boolean flag){
        ResultVo<Object> resultVo = new ResultVo<>();
        resultVo.setCode(ResultEnum.SUCCESS.getCode());
        resultVo.setMessage(msg);
        resultVo.setSuccess(flag);
        return resultVo;
    }

    /**
     * 响应请求失败数据实体（不含返回数据）
     * @param msg
     * @param flag
     * @return
     */
    public static ResultVo error(String msg, boolean flag){
        ResultVo<Object> resultVo = new ResultVo<>();
        resultVo.setCode(ResultEnum.ERROR.getCode());
        resultVo.setMessage(msg);
        resultVo.setSuccess(flag);
        return resultVo;
    }
}
