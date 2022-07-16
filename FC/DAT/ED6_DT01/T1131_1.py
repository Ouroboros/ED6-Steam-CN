import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T1131_1_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T1131_1 ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'T1131.x'
    header.mapIndex       = 1
    header.bgm            = 11
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0xA49
@scena.StringTable('StringTable')
def StringTable():
    return stringTable

# id: 0x10000 offset: 0x64
@scena.EntryPoint('EntryPoint')
def EntryPoint():
    return (
    )

# id: 0x10001 offset: 0x64
@scena.ChipData('ChipData')
def ChipData():
    return [
        # (ch, cp)
    ]

# id: 0x10002 offset: 0x64
@scena.NpcData('NpcData')
def NpcData():
    return (
    )

# id: 0x10003 offset: 0x64
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x64
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x64
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x64
@scena.Code('PreInit')
def PreInit():
    ChrTalk(
        0x00FE,
        (
            '#1350150889V哎呀，有什么事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_D6',
    )

    ChrTalk(
        0x0101,
        (
            '#0010150890V#508F谢谢惠顾～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010150891V这是您委托游击士协会的东西～\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_173')

    def _loc_D6(): pass

    label('loc_D6')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_126',
    )

    ChrTalk(
        0x0102,
        (
            '#0020150892V#010F您是格露娜小姐吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020150893V我们给您送东西来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_173')

    def _loc_126(): pass

    label('loc_126')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_173',
    )

    ChrTalk(
        0x0103,
        (
            '#0030150894V#020F您是格露娜小姐吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030150895V我们给您送东西来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_173(): pass

    label('loc_173')

    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '交出了５个',
            (TxtCtl.SetColor, 0x2),
            '魔兽鸟肉',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    RemoveItem(0x03A7, 5)

    ChrTalk(
        0x00FE,
        (
            '#1350150896V啊，真是太感谢了，\n',
            '还让你们特地跑了一趟。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1350150897V你们很忙吧，\n',
            '给你们添麻烦了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010150898V#006F没有啦，完全没那回事。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010150899V帮助有困难的人，\n',
            '是我们游击士的工作嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030150900V#020F对，艾丝蒂尔说得没错。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030150901V而且现在还正处于\n',
            '定期船停航的非常时期。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0103, 400)

    ChrTalk(
        0x00FE,
        (
            '#1350150902V谢谢你们，\n',
            '这样说让我宽心了不少。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1350150903V不过，\n',
            '用金钱并不足以表达我的谢意……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x00FE, 0x00000000, 2000, 0x22, 0x24, 0x000000FA, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(800)

    ChrTalk(
        0x00FE,
        (
            '#1350150904V………………对了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1350150905V请你们再接受\n',
            '我的一份谢礼好吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010150906V#004F啊？是什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '#1350150907V我把我们店里最受欢迎的一道菜——\n',
            '『王国煎蛋卷』的制作方法教给你们吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010150908V#004F我们店，\n',
            '是指这个安特洛丝餐厅吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1350150909V嗯，当然了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010150910V#000F这样好吗？\n',
            '把料理的菜谱告诉我们……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1350150911V不用担心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1350150912V即使知道菜谱，\n',
            '也不一定能做出原汁原味的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0103, 0x00FE, 400)

    ChrTalk(
        0x0103,
        (
            '#0030150913V#020F很有自信嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0103, 400)

    ChrTalk(
        0x00FE,
        (
            '#1350150914V呵呵，因为这不仅是\n',
            '精不精通于做菜的问题哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1350150915V打个比方，\n',
            '就好像乐谱和音乐家的关系一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1350150916V同样的乐谱也会因为演奏者的不同，\n',
            '而产生不一样的效果。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010150917V#505F呼～真是深奥啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '#1350150918V菜谱是最终制作出\n',
            '美味菜肴的条件之一。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1350150919V你们可以保持原有的简单配料，\n',
            '然后去尝试改变它的味道，\n',
            '说不定会有意想不到的效果哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeOut(300, 0, 100)
    OP_0D()

    If(
        (
            (Expr.Eval, "OP_40(0x020D)"),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_6D4',
    )

    If(
        (
            (Expr.Eval, "OP_AC(0x000C)"),
            Expr.Return,
        ),
        'loc_6AC',
    )

    Jump('loc_6D4')

    def _loc_6AC(): pass

    label('loc_6AC')

    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            TxtCtl.ShowAll,
            (TxtCtl.SetColor, 0x0),
            '学会了',
            (TxtCtl.SetColor, 0x2),
            '王国煎蛋卷',
            (TxtCtl.SetColor, 0x0),
            '的做法。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6D4(): pass

    label('loc_6D4')

    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_62(0x0101, 0x00000000, 2000, 0x08, 0x09, 0x000000FA, 0x02)
    PlaySE(15, 0x00, 0x64)
    Sleep(800)

    ChrTalk(
        0x0101,
        (
            '#0010150920V#001F哈哈㈱　太好了～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010150921V好，\n',
            '我马上就试着做做看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020150486V#018F……………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020150923V……艾丝蒂尔，拜托，\n',
            '你能不能把菜谱仔细研究之后再做？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x0C, 0x0D, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    ChrTurnDirection(0x0101, 0x0102, 400)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010150924V#005F你、你这是什么话～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010150925V岂有此理，\n',
            '你好像在说我不会做饭一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020150926V#017F你这样说的话，\n',
            '就更要好好注意调味料的量才行啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020150927V因为艾丝蒂尔你\n',
            '经常一放就是一大堆呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x0E, 0x0F, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010150421V#009F哼。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '#1350150929V好啦好啦，制作方法固然重要，\n',
            '不过最重要的还是能享受美味的料理吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1350150930V说不定品尝之后\n',
            '就能知道其中的诀窍了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x00FE, 400)

    ChrTalk(
        0x0101,
        (
            '#0010150931V#001F嗯，的确是这样⊙',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010150932V谢谢你给我们这么多指点。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1350150933V彼此彼此。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1350150934V请你们有空也到本店\n',
            '品尝其他美味的料理哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(23, 0x00, 0x64)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '任务【收集食物材料】',
            (TxtCtl.SetColor, 0x0),
            '完成！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_28(0x0012, 0x04, 0x10)
    SetScenaFlags(ScenaFlag(0x0001, 2, 0xA))
    OP_28(0x0012, 0x01, 0x0001)
    TalkEnd(0x0011)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
