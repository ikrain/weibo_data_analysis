package cn.krain.weibo_data_analysis_web.dao;

import cn.krain.weibo_data_analysis_web.entity.SystemSensitiveWord;

import java.util.List;
import java.util.Map;

/**
 * @author cc
 * @data 2022/5/5 - 22:54
 */
public interface SystemSensitiveWordDao {
    List<SystemSensitiveWord> selectSensitiveWord();

    void insertSenWord(SystemSensitiveWord sensitiveWord);

    void deleteSenWord(String id);
}
