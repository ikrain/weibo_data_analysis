package cn.krain.weibo_data_analysis_web.web.controller;

import cn.krain.weibo_data_analysis_web.entity.SystemArticleComment;
import cn.krain.weibo_data_analysis_web.entity.SystemWeekRank;
import cn.krain.weibo_data_analysis_web.result.ResultUtil;
import cn.krain.weibo_data_analysis_web.service.SystemArticleCommentService;
import cn.krain.weibo_data_analysis_web.service.SystemWeekRankService;
import cn.krain.weibo_data_analysis_web.vo.SystemSearchTopicVo;
import cn.krain.weibo_data_analysis_web.vo.SystemWeekRankVo;
import com.alibaba.fastjson.JSONObject;
import io.swagger.annotations.Api;
import io.swagger.annotations.ApiOperation;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * @author cc
 * @data 2022/5/10 - 18:35
 */
@Api("系统情感分析数据展示接口")
@Controller
@ResponseBody
@RequestMapping("/emotion")
public class SystemEmotionController {
    @Autowired
    private SystemArticleCommentService systemArticleCommentService;

    @GetMapping("/queryCommentEmotion")
    @ApiOperation("查询情感分析数据")
    public Object queryCommentEmotion(String topic_name){
        try {
            Map<String, Object> map = new HashMap<>();
            map.put("topic_name", topic_name);
            List<SystemArticleComment> articleCommentList = systemArticleCommentService.queryCommentEmotion(map);
            JSONObject resultData = new JSONObject();
            resultData.put("articleCommentList", articleCommentList);
            return ResultUtil.success("查询情感分析数据成功", resultData, true);
        }catch (Exception e){
            e.printStackTrace();
            // 登录失败返回提示信息
            return ResultUtil.error("查询情感分析数据失败", false);
        }
    }

    @GetMapping("/queryCommEmoByPage")
    @ApiOperation("查询评论情感列表数据")
    public Object queryCommEmoByPage(String page, String limit, String topic_name){
        try {
            Map<String, Object> map = new HashMap<>();
            //更具page和limit来计算跳跃的数字  (limit 0,3)
            int pageInt = Integer.valueOf(page);
            int limitInt = Integer.valueOf(limit);
            int skipCount = (pageInt - 1) * limitInt;
            map.put("skipCount", skipCount);
            map.put("limit", limitInt);
            map.put("topic_name", topic_name);
            List<SystemArticleComment> articleCommentList = systemArticleCommentService.queryCommEmoList(map);
            int total = systemArticleCommentService.getTotalByTopicName(map);
            JSONObject resultData = new JSONObject();
            resultData.put("articleCommentList", articleCommentList);
            resultData.put("total", total);
            return ResultUtil.success("查询评论情感列表数据成功", resultData, true);
        }catch (Exception e){
            e.printStackTrace();
            // 登录失败返回提示信息
            return ResultUtil.error("查询评论情感列表数据失败", false);
        }
    }

}
