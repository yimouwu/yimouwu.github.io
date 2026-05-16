# Assets Guide — 你需要准备的所有素材

## 📸 照片 (放在 `assets/images/`)

| 文件名 | 尺寸建议 | 说明 |
|--------|----------|------|
| `profile.jpg` | 500×500px，正方形 | **头像**，会被裁成圆形显示。建议用白/浅色/自然背景，清晰正面或3/4侧脸照 |
| `pub_paper1.jpg` | 260×180px，16:9 | 第1篇论文的**缩略图**，可截取论文首图/方法图 |
| `pub_paper2.jpg` | 260×180px，16:9 | 第2篇论文缩略图 |
| `pub_paper3.jpg` | 260×180px，16:9 | 第3篇论文缩略图 |
| `proj_1.jpg` | 480×300px | 项目1封面图 |
| `proj_2.jpg` | 480×300px | 项目2封面图 |
| `proj_3.jpg` | 480×300px | 项目3封面图 |
| `talk1_thumb.jpg` | 400×225px，16:9 | Talk 1 视频封面（可截取 YouTube 缩略图） |
| `talk2_thumb.jpg` | 400×225px，16:9 | Talk 2 视频封面 |

> **提示**：所有图片如果缺失，网站会自动优雅降级（显示占位符），不会报错。

---

## 🎬 视频 (放在 `assets/videos/`)

| 文件名 | 说明 |
|--------|------|
| `talk1.mp4` | 演讲/Demo 视频（可选，也可以直接用 YouTube 链接） |
| `talk2.mp4` | 演讲/Demo 视频2 |

> **YouTube 视频**：在 `index.html` 的 talks 区域，把 `VIDEO_ID` 替换成 YouTube 链接里 `?v=` 后面的那串 ID 即可，无需下载视频。

---

## 📄 PDF (放在 `assets/pdf/`)

| 文件名 | 说明 |
|--------|------|
| `cv.pdf` | 你的简历 CV |

---

## ✏️ 需要在 index.html 中修改的文字内容

- `[Your University]` → 你的大学名称
- `[Advisor Name]` → 导师姓名
- `[Undergraduate University]` → 本科学校
- `your@email.com` → 你的邮箱
- `github.com/yimouwu` → 你的 GitHub 主页
- 论文标题、作者、venue → 替换成你真实的论文
- 项目名称和描述 → 替换成你的项目
- 页脚引言 → 可以换成你喜欢的哲学名言