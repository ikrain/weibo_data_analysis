package cn.krain.weibo_data_analysis_web.web.controller;

import cn.krain.weibo_data_analysis_web.entity.SystemCommentMap;
import cn.krain.weibo_data_analysis_web.entity.SystemUser;
import cn.krain.weibo_data_analysis_web.result.ResultUtil;
import cn.krain.weibo_data_analysis_web.service.SystemCommentMapService;
import cn.krain.weibo_data_analysis_web.service.SystemTimeService;
import cn.krain.weibo_data_analysis_web.service.SystemTopicAreaService;
import cn.krain.weibo_data_analysis_web.service.SystemUserService;
import cn.krain.weibo_data_analysis_web.util.MD5Util;
import cn.krain.weibo_data_analysis_web.vo.*;
import com.alibaba.fastjson.JSONObject;
import io.swagger.annotations.Api;
import io.swagger.annotations.ApiImplicitParam;
import io.swagger.annotations.ApiImplicitParams;
import io.swagger.annotations.ApiOperation;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.*;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * @author cc
 * @data 2022/5/10 - 18:35
 */
@Api("系统首页数据展示接口")
@Controller
@ResponseBody
@RequestMapping("/home")
public class SystemHomeController {
    @Autowired
    private SystemCommentMapService systemCommentMapService;

    @Autowired
    private SystemTopicAreaService systemTopicAreaService;

    @Autowired
    private SystemTimeService systemTimeService;

    @GetMapping("/queryMap")
    @ApiOperation("查询活跃评论地图数据")
    public Object query_map(){
        try {
            List<SystemCommentMapVo> mapListVo = systemCommentMapService.queryCommentMap();
            JSONObject resultData = new JSONObject();
            resultData.put("mapListVo", mapListVo);
            return ResultUtil.success("查询地图数据成功", resultData, true);
        }catch (Exception e){
            e.printStackTrace();
            // 登录失败返回提示信息
            return ResultUtil.error("查询地图数据失败", false);
        }
    }

    @GetMapping("/queryTopicArea")
    @ApiOperation("查询话题领域饼状图数据")
    public Object query_topic_area(){
        try {
            List<SystemTopicAreaVo> topicAreaVo = systemTopicAreaService.queryTopicAreaVo();
            JSONObject resultData = new JSONObject();
            resultData.put("topicAreaVo", topicAreaVo);
            return ResultUtil.success("查询饼状图数据成功", resultData, true);
        }catch (Exception e){
            e.printStackTrace();
            // 登录失败返回提示信息
            return ResultUtil.error("查询饼状图数据失败", false);
        }
    }


    @GetMapping("/queryTopicTime")
    public Object query_topic_time(){
        try {
            List<TopicTimeVo> topicTimeVoList = systemTimeService.queryTopicTime();
            JSONObject resultData = new JSONObject();
            resultData.put("topicTimeVoList", topicTimeVoList);
            return ResultUtil.success("查询数据成功", resultData, true);
        }catch (Exception e){
            e.printStackTrace();
            // 登录失败返回提示信息
            return ResultUtil.error("查询数据失败", false);
        }
    }

    @GetMapping("/queryArticleTime")
    public Object query_article_time(){
        try {
            List<ArticleTimeVo> articleTimeVoList = systemTimeService.queryArticleTime();
            JSONObject resultData = new JSONObject();
            resultData.put("articleTimeVoList", articleTimeVoList);
            return ResultUtil.success("查询数据成功", resultData, true);
        }catch (Exception e){
            e.printStackTrace();
            // 登录失败返回提示信息
            return ResultUtil.error("查询数据失败", false);
        }
    }

    @GetMapping("/queryCommentTime")
    public Object query_comment_time(){
        try {
            List<CommentTimeVo> commentTimeVoList = systemTimeService.queryCommentTime();
            JSONObject resultData = new JSONObject();
            resultData.put("commentTimeVoList", commentTimeVoList);
            return ResultUtil.success("查询数据成功", resultData, true);
        }catch (Exception e){
            e.printStackTrace();
            // 登录失败返回提示信息
            return ResultUtil.error("查询数据失败", false);
        }
    }

    @GetMapping("/queryTopicNum")
    public Object query_topic_num(){
        try {
            int topicNum = systemTimeService.queryTopicNum();
            JSONObject resultData = new JSONObject();
            resultData.put("topicNum", topicNum);
            return ResultUtil.success("查询数据成功", resultData, true);
        }catch (Exception e){
            e.printStackTrace();
            // 登录失败返回提示信息
            return ResultUtil.error("查询数据失败", false);
        }
    }

    @GetMapping("/queryArticleNum")
    public Object query_article_num(){
        try {
            int articleNum = systemTimeService.queryArticleNum();
            JSONObject resultData = new JSONObject();
            resultData.put("articleNum", articleNum);
            return ResultUtil.success("查询数据成功", resultData, true);
        }catch (Exception e){
            e.printStackTrace();
            // 登录失败返回提示信息
            return ResultUtil.error("查询数据失败", false);
        }
    }

    @GetMapping("/queryTopicAddNum")
    public Object query_topic_add_num(){
        try {
            int topicAddNum = systemTimeService.queryTopicAddNum();
            JSONObject resultData = new JSONObject();
            resultData.put("topicAddNum", topicAddNum);
            return ResultUtil.success("查询数据成功", resultData, true);
        }catch (Exception e){
            e.printStackTrace();
            // 登录失败返回提示信息
            return ResultUtil.error("查询数据失败", false);
        }
    }

    @GetMapping("/queryArticleAddNum")
    public Object query_article_add_num(){
        try {
            int articleAddNum = systemTimeService.queryArticleAddNum();
            JSONObject resultData = new JSONObject();
            resultData.put("articleAddNum", articleAddNum);
            return ResultUtil.success("查询数据成功", resultData, true);
        }catch (Exception e){
            e.printStackTrace();
            // 登录失败返回提示信息
            return ResultUtil.error("查询数据失败", false);
        }
    }

}
