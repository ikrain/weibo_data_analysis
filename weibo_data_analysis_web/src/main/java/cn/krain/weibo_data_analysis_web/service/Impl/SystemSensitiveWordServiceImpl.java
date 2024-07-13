package cn.krain.weibo_data_analysis_web.service.Impl;

import cn.krain.weibo_data_analysis_web.dao.SystemSensitiveWordDao;
import cn.krain.weibo_data_analysis_web.entity.SystemSensitiveWord;
import cn.krain.weibo_data_analysis_web.service.SystemSensitiveWordService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

/**
 * @author cc
 * @data 2022/5/13 - 16:00
 */
@Service
public class SystemSensitiveWordServiceImpl implements SystemSensitiveWordService {

    @Autowired
    private SystemSensitiveWordDao sensitiveWordDao;

    @Override
    public List<SystemSensitiveWord> getAllSenWord() {
        return sensitiveWordDao.selectSensitiveWord();
    }

    @Override
    public void delSenWordById(String id) {
        sensitiveWordDao.deleteSenWord(id);
    }

    @Override
    public void addSenWord(SystemSensitiveWord sensitiveWord) {
        sensitiveWordDao.insertSenWord(sensitiveWord);
    }
}
