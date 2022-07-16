import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T0510_1_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T0510_1 ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'T0510.x'
    header.mapIndex       = 18
    header.bgm            = 16
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0xAB8
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
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0050, 1, 0x281)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_357',
    )

    SetScenaFlags(ScenaFlag(0x0050, 1, 0x281))

    ChrTalk(
        0x0008,
        (
            '#1130150292V哦哦，\n',
            '这不是艾丝蒂尔和约修亚吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0008, 0)

    ChrTalk(
        0x0101,
        (
            '#0010150293V#000F阿斯顿队长，你好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0008, 0)

    ChrTalk(
        0x0102,
        (
            '#0020150294V#010F很久不见了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1130150295V啊啊，好久不见了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1130150296V我都听说了，\n',
            '我家的鲁克给你们添了不少麻烦呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1130150297V作为父亲，真是感到惭愧啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010150298V#001F没事，像他这种年纪的男孩子\n',
            '喜欢恶作剧也是没有办法的事。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010150299V#001F就算是我，\n',
            '小的时候也经常到城镇外面乱跑呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020150300V#017F你不是女孩子吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1130150301V哈哈，还是这么精神啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1130150302V你这种精神劲头\n',
            '要是也能分一部分\n',
            '给这里的新兵就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1130150303V我想通过模拟战斗来锻炼那些新兵，\n',
            '并端正他们的态度。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1130150304V于是我就通过\n',
            '游击士协会募集\n',
            '愿意扮演敌兵角色的人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1130150305V如果能由你们来扮演就再合适不过了，\n',
            '怎么样？可以吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x0008, 0x04, 0x04)
    OP_28(0x0008, 0x01, 0x0001)
    OP_28(0x0008, 0x04, 0x02)
    ChrTurnDirection(0x0102, 0x0008, 400)

    Jump('loc_4EE')

    def _loc_357(): pass

    label('loc_357')

    If(
        (
            (Expr.Eval, "OP_29(0x0008, 0x01, 0x8000)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4A3',
    )

    ChrTalk(
        0x0008,
        (
            '#1130150306V哦，是艾丝蒂尔和约修亚啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1130150307V你们是因为看到了\n',
            '协会的公告板而赶来的吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1130150308V实际上是这样的，\n',
            '我想通过模拟战斗来锻炼那些新兵，\n',
            '并端正他们的态度。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1130150309V于是我就通过\n',
            '游击士协会募集\n',
            '愿意扮演敌兵角色的人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1130150305V如果能由你们来扮演就再合适不过了，\n',
            '怎么样？可以吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x0008, 0x04, 0x04)
    OP_28(0x0008, 0x01, 0x0001)
    OP_28(0x0008, 0x04, 0x02)

    Jump('loc_4EE')

    def _loc_4A3(): pass

    label('loc_4A3')

    ChrTalk(
        0x0008,
        (
            '#1130150311V事情办完了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1130150312V可以来扮演\n',
            '模拟战斗的敌兵角色了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4EE(): pass

    label('loc_4EE')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_7C4',
    )

    FadeOut(300, 0, 100)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Menu(
        0,
        10,
        10,
        0,
        (
            TXT(0x00, '【接受】\n'),
            TXT(0x01, '【拒绝】\n'),
        ),
    )

    MenuEnd(0x0000)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0000)
    FadeIn(300, 0)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000001, 'loc_552'),
        (0x00000000, 'loc_631'),
        (-1, 'loc_552'),
    )

    def _loc_552(): pass

    label('loc_552')

    OP_28(0x0008, 0x01, 0x8000)

    ChrTalk(
        0x0101,
        (
            '#0010150313V#505F对不起啊，阿斯顿队长。\n',
            '我们还有事情要办……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1130150314V这样啊，真是遗憾啊，\n',
            '不过我是不会勉强你们的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1130150315V如果愿意帮忙的话，\n',
            '就请尽快到这里来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010150316V#000F嗯，知道了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0000)

    Jump('loc_7C1')

    def _loc_631(): pass

    label('loc_631')

    OP_28(0x0008, 0x04, 0x08)

    ChrTalk(
        0x0101,
        (
            '#0010150317V#006F嗯，可以。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020150318V#010F我们接受。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1130150319V谢谢，真是帮大忙了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1130150320V在训练的准备完成之前\n',
            '你们就先休息一会儿吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1130150321V如果不保持最好的状态去训练，\n',
            '就没有什么效果了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x08, 0x09, 0x000000FA, 0x02)
    PlaySE(15, 0x00, 0x64)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010150322V#001F好的～～\n',
            '那我就先小睡一觉啦～～⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020150323V#010F那我们就去准备了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1130150324V嗯，有劳你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(3000, 0, -1)
    OP_0D()
    SetChrStatus(0x0000, 0xFE, 0)
    SetChrStatus(0x0001, 0xFE, 0)
    NewScene('ED6_DT01/T0500._SN', 1, 0, 0)
    IdleLoop()

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0000)

    Jump('loc_7C1')

    def _loc_7C1(): pass

    label('loc_7C1')

    Jump('loc_4EE')

    def _loc_7C4(): pass

    label('loc_7C4')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0001 offset: 0x7CF
@scena.Code('Init')
def Init():
    TalkBegin(0x0008)
    EventBegin(0x00)
    CameraMove(28890, 0, -73240, 0)
    SetChrDirection(0x0008, 270, 0)
    SetChrPos(0x0101, 27710, 0, -72870, 90)
    SetChrPos(0x0102, 27790, 0, -73700, 90)
    SetChrStatus(0x0000, 0xFE, 0)
    SetChrStatus(0x0001, 0xFE, 0)
    Sleep(2000)

    ChrTalk(
        0x0008,
        (
            '#1130150372V艾丝蒂尔、约修亚，\n',
            '今天真是辛苦你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1130150373V通过你们的协助，\n',
            '士兵们或多或少明白了一些道理。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0008, 0)

    ChrTalk(
        0x0101,
        (
            '#0010150374V#000F您太客气了，\n',
            '说谢谢的应该是我们才对。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010150375V这是一次很好的锻炼呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0008, 0)

    ChrTalk(
        0x0102,
        (
            '#0020150376V#010F是啊，我们也学到了很多。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1130150377V呵呵，你们能够有这种想法，\n',
            '今后肯定会成为杰出的游击士的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1130150378V能站在对方的角度去思考，\n',
            '就可以非常的客观公正了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1130150379V希望你们能够在今后的舞台中大展身手。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010150380V#001F嗯。\n',
            '谢谢你，阿斯顿队长。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020150381V#010F阿斯顿队长也要好好保重。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1130150382V嗯。\n',
            '那么，再会了。',
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
            '任务【训练士兵】',
            (TxtCtl.SetColor, 0x0),
            '完成！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))
    OP_28(0x0008, 0x04, 0x10)
    OP_28(0x0008, 0x01, 0x0008)
    SetChrStatus(0x0000, 0xFE, 0)
    SetChrStatus(0x0001, 0xFE, 0)
    EventEnd(0x00)
    ClearMapFlags(0x00400000)
    TalkEnd(0x0008)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
