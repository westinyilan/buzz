---
title: 翻译功能
---

默认的“翻译”任务借助 Whisper 模型将内容翻译成英语。从 `1.0.0` 版本开始，Buzz 支持使用其他人工智能将内容翻译成任意语言。

若要使用翻译功能，你需要配置 OpenAI API 密钥和翻译设置。在“偏好设置”中设置 OpenAI API 密钥。Buzz 也支持本地运行的、兼容 OpenAI API 的自定义翻译人工智能。有关本地运行人工智能的更多信息，请参阅 [ollama](https://ollama.com/blog/openai-compatibility) 或 [LM Studio](https://lmstudio.ai/)。有关可用自定义 API 的信息，请查看这个 [讨论线程](https://github.com/chidiwilliams/buzz/discussions/827)。

若要为实时录制配置翻译功能，可在实时录制设置的“高级设置”对话框中启用该功能。输入要使用的人工智能模型，并提供给人工智能的翻译指令提示。对于已经完成语音识别的文件，也可以使用翻译功能。在转录查看器工具栏上点击“翻译”按钮即可。

为了让人工智能知道如何进行翻译，请在“给人工智能的指令”部分输入翻译说明。在说明中，你应该明确指出要将文本翻译成何种语言。此外，由于人工智能往往会添加一些注释或备注，你可能需要额外添加指令禁止其这么做。以下是一个将英语字幕翻译成西班牙语的指令示例：

> 你是一位专业翻译人员，擅长将英语翻译成西班牙语。你只需将发给你的每一句话翻译成西班牙语，不要添加任何注释或备注。

如果你在“偏好设置”中启用了“启用实时录制转录导出”功能，实时文本转录内容在生成和翻译后将被导出到一个文本文件中。这个文件可用于将实时转录内容与其他应用程序（如 OBS Studio）进行进一步集成。

使用 ChatGPT `gpt - 4o` 模型对一小时长的音频进行翻译，大致费用约为 0.50 美元。
