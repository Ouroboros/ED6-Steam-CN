import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T1130_1_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T1130_1 ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'T1130.x'
    header.mapIndex       = 1
    header.bgm            = 11
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x1001
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
    ClearMapFlags(0x00000001)
    EventBegin(0x00)
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))
    OP_28(0x000D, 0x04, 0x10)
    RemoveItem(0x0329, 1)

    If(
        (
            (Expr.GetChrWork, 0x0, 0x1),
            (Expr.PushLong, 0xE6DC),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_44C',
    )

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1CB',
    )

    Fade(1000)
    SetChrPos(0x0101, 60600, 1000, 52500, 270)
    SetChrPos(0x0102, 60600, 1000, 51300, 315)
    SetChrPos(0x0103, 61600, 1000, 51500, 270)

    If(
        (
            (Expr.Eval, "OP_42(0x0003)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_EC',
    )

    SetChrPos(0x0104, 61600, 1000, 50200, 315)

    Jump('loc_10B')

    def _loc_EC(): pass

    label('loc_EC')

    If(
        (
            (Expr.Eval, "OP_42(0x0033)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_10B',
    )

    SetChrPos(0x0134, 61600, 1000, 50200, 315)

    def _loc_10B(): pass

    label('loc_10B')

    ChrTurnDirection(0x0101, 0x0008, 0)
    OP_69(0x0101, 2000)

    ChrTalk(
        0x0101,
        (
            '#0010150830V#000F那个～可以打扰一下吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkBegin(0x0008)

    ChrTalk(
        0x0008,
        (
            '#1340150831V嗯？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010150832V#000F您是豪尔斯教区长吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1340150833V呵～呵～呵。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1340150834V我就是豪尔斯没错啊……\n',
            '找我有什么事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_449')

    def _loc_1CB(): pass

    label('loc_1CB')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2A2',
    )

    Fade(1000)
    SetChrPos(0x0102, 60600, 1000, 52500, 270)
    SetChrPos(0x0101, 60600, 1000, 51300, 315)
    SetChrPos(0x0103, 61600, 1000, 51500, 270)

    If(
        (
            (Expr.Eval, "OP_42(0x0003)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_231',
    )

    SetChrPos(0x0104, 61600, 1000, 50200, 315)

    Jump('loc_250')

    def _loc_231(): pass

    label('loc_231')

    If(
        (
            (Expr.Eval, "OP_42(0x0033)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_250',
    )

    SetChrPos(0x0134, 61600, 1000, 50200, 315)

    def _loc_250(): pass

    label('loc_250')

    ChrTurnDirection(0x0102, 0x0008, 0)
    OP_69(0x0102, 2000)

    ChrTalk(
        0x0102,
        (
            '#0020150835V#010F教区长，\n',
            '可以打扰您一下吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkBegin(0x0008)

    ChrTalk(
        0x0008,
        (
            '#1340150831V嗯？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_449')

    def _loc_2A2(): pass

    label('loc_2A2')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_379',
    )

    Fade(1000)
    SetChrPos(0x0103, 60600, 1000, 52500, 270)
    SetChrPos(0x0101, 60600, 1000, 51300, 315)
    SetChrPos(0x0102, 61600, 1000, 51500, 270)

    If(
        (
            (Expr.Eval, "OP_42(0x0003)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_308',
    )

    SetChrPos(0x0104, 61600, 1000, 50200, 315)

    Jump('loc_327')

    def _loc_308(): pass

    label('loc_308')

    If(
        (
            (Expr.Eval, "OP_42(0x0033)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_327',
    )

    SetChrPos(0x0134, 61600, 1000, 50200, 315)

    def _loc_327(): pass

    label('loc_327')

    ChrTurnDirection(0x0103, 0x0008, 0)
    OP_69(0x0103, 2000)

    ChrTalk(
        0x0103,
        (
            '#0030150837V#020F教区长，\n',
            '可以打扰您一下吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkBegin(0x0008)

    ChrTalk(
        0x0008,
        (
            '#1340150831V嗯？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_449')

    def _loc_379(): pass

    label('loc_379')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_449',
    )

    Fade(1000)
    SetChrPos(0x0104, 60600, 1000, 52500, 270)
    SetChrPos(0x0101, 60600, 1000, 51300, 315)
    SetChrPos(0x0103, 61600, 1000, 50200, 315)
    SetChrPos(0x0102, 61600, 1000, 51500, 270)
    ChrTurnDirection(0x0104, 0x0008, 0)
    OP_69(0x0104, 2000)

    ChrTalk(
        0x0104,
        (
            '#0040150839V#030F哟，亲爱的教区长您好啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040150840V不好意思，\n',
            '不知道能不能和你聊几句呢。 ',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkBegin(0x0008)

    ChrTalk(
        0x0008,
        (
            '#1340150831V嗯？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_449(): pass

    label('loc_449')

    Jump('loc_80F')

    def _loc_44C(): pass

    label('loc_44C')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_591',
    )

    Fade(1000)
    SetChrPos(0x0101, 57400, 1000, 52500, 90)
    SetChrPos(0x0102, 57400, 1000, 51300, 45)
    SetChrPos(0x0103, 56400, 1000, 51500, 90)

    If(
        (
            (Expr.Eval, "OP_42(0x0003)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4B2',
    )

    SetChrPos(0x0104, 56400, 1000, 50200, 45)

    Jump('loc_4D1')

    def _loc_4B2(): pass

    label('loc_4B2')

    If(
        (
            (Expr.Eval, "OP_42(0x0033)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4D1',
    )

    SetChrPos(0x0134, 56400, 1000, 50200, 45)

    def _loc_4D1(): pass

    label('loc_4D1')

    ChrTurnDirection(0x0101, 0x0008, 0)
    OP_69(0x0101, 2000)

    ChrTalk(
        0x0101,
        (
            '#0010150830V#000F那个～可以打扰一下吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkBegin(0x0008)

    ChrTalk(
        0x0008,
        (
            '#1340150831V嗯？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010150832V#000F您是豪尔斯教区长吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1340150833V呵～呵～呵。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1340150834V我就是豪尔斯没错啊……\n',
            '找我有什么事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_80F')

    def _loc_591(): pass

    label('loc_591')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_668',
    )

    Fade(1000)
    SetChrPos(0x0102, 57400, 1000, 52500, 90)
    SetChrPos(0x0101, 57400, 1000, 51300, 45)
    SetChrPos(0x0103, 56400, 1000, 51500, 90)

    If(
        (
            (Expr.Eval, "OP_42(0x0003)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_5F7',
    )

    SetChrPos(0x0104, 56400, 1000, 50200, 45)

    Jump('loc_616')

    def _loc_5F7(): pass

    label('loc_5F7')

    If(
        (
            (Expr.Eval, "OP_42(0x0033)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_616',
    )

    SetChrPos(0x0134, 56400, 1000, 50200, 45)

    def _loc_616(): pass

    label('loc_616')

    ChrTurnDirection(0x0102, 0x0008, 0)
    OP_69(0x0102, 2000)

    ChrTalk(
        0x0102,
        (
            '#0020150835V#010F教区长，\n',
            '可以打扰您一下吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkBegin(0x0008)

    ChrTalk(
        0x0008,
        (
            '#1340150831V嗯？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_80F')

    def _loc_668(): pass

    label('loc_668')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_73F',
    )

    Fade(1000)
    SetChrPos(0x0103, 57400, 1000, 52500, 90)
    SetChrPos(0x0101, 57400, 1000, 51300, 45)
    SetChrPos(0x0102, 56400, 1000, 51500, 90)

    If(
        (
            (Expr.Eval, "OP_42(0x0003)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_6CE',
    )

    SetChrPos(0x0104, 56400, 1000, 50200, 45)

    Jump('loc_6ED')

    def _loc_6CE(): pass

    label('loc_6CE')

    If(
        (
            (Expr.Eval, "OP_42(0x0033)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_6ED',
    )

    SetChrPos(0x0134, 56400, 1000, 50200, 45)

    def _loc_6ED(): pass

    label('loc_6ED')

    ChrTurnDirection(0x0103, 0x0008, 0)
    OP_69(0x0103, 2000)

    ChrTalk(
        0x0103,
        (
            '#0030150837V#020F教区长，\n',
            '可以打扰您一下吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkBegin(0x0008)

    ChrTalk(
        0x0008,
        (
            '#1340150831V嗯？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_80F')

    def _loc_73F(): pass

    label('loc_73F')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_80F',
    )

    Fade(1000)
    SetChrPos(0x0104, 57400, 1000, 52500, 90)
    SetChrPos(0x0101, 57400, 1000, 51300, 45)
    SetChrPos(0x0103, 56400, 1000, 50200, 45)
    SetChrPos(0x0102, 56400, 1000, 51500, 90)
    ChrTurnDirection(0x0104, 0x0008, 0)
    OP_69(0x0104, 2000)

    ChrTalk(
        0x0104,
        (
            '#0040150839V#030F哟，亲爱的教区长您好啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040150840V不好意思，\n',
            '不知道能不能和你聊几句呢。 ',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkBegin(0x0008)

    ChrTalk(
        0x0008,
        (
            '#1340150831V嗯？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_80F(): pass

    label('loc_80F')

    ChrTalk(
        0x0101,
        (
            '#0010150854V#000F请收下这个。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010150855V这是洛连特的迪拜恩教区长\n',
            '要我转交给您的一封信。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '交出了',
            (TxtCtl.SetColor, 0x2),
            '教区长的亲笔信',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 2, 0x312)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_8C1',
    )

    OP_28(0x000D, 0x01, 0x4000)

    def _loc_8C1(): pass

    label('loc_8C1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 3, 0x32B)),
            Expr.Return,
        ),
        'loc_91B',
    )

    OP_28(0x000D, 0x01, 0x2000)
    OP_28(0x000D, 0x01, 0x0002)

    ChrTalk(
        0x0101,
        (
            '#0010150856V#000F抱歉，因为有一些事情，\n',
            '送来的时间稍微晚了一些。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_921')

    def _loc_91B(): pass

    label('loc_91B')

    OP_28(0x000D, 0x01, 0x0004)

    def _loc_921(): pass

    label('loc_921')

    ChrTurnDirection(0x0008, 0x0101, 400)

    ChrTalk(
        0x0008,
        (
            '#1340150857V呵～呵～呵。\n',
            '哎呀，真是辛苦你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1340150858V那么我就收下了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1340150859V我先看看\n',
            '这封信到底写了些什么……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1340150860V迪拜恩教区长又在\n',
            '设计一种新的配药方法了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010150861V#501F…………嗯？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010150862V配药方法……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0101, 0)

    ChrTalk(
        0x0008,
        (
            '#1340150863V呵～呵～呵。\n',
            '难道你不知道吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1340150864V迪拜恩教区长可以说是利贝尔无人不知、\n',
            '无人不晓的药学大师哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1340150865V在进入大圣堂之前\n',
            '就已经声名远扬了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010150866V#004F啊！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1340150867V迪拜恩教区长到洛连特任职之后，\n',
            '研究还是从未间断过……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1340150868V一旦发现了疗效颇佳的药材，\n',
            '总会像这样来通知我们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x0002)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_BF9',
    )

    ChrTalk(
        0x0103,
        (
            '#0030150869V#020F教区长调制出的新药，\n',
            '对我们这些游击士来说\n',
            '的确是非常有用。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030150870V总是在我们忙于工作的时候\n',
            '默默保护着我们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_BF9(): pass

    label('loc_BF9')

    ChrTalk(
        0x0101,
        (
            '#0010150871V#004F……这样的事情我居然不知道。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010150872V真是的……\n',
            '为什么我从来都没听他说过呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020150873V#010F教区长一直都是如此。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020150874V他很少和别人说起\n',
            '关于他自己的事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010150875V#000F嗯，原来是这样啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x0003)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_DDF',
    )

    ChrTurnDirection(0x0101, 0x0104, 400)

    ChrTalk(
        0x0101,
        (
            '#0010150876V#509F和某个口出狂言\n',
            '尽说些不着边际的话的人完全不一样。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0104, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    ChrTurnDirection(0x0104, 0x0101, 400)

    ChrTalk(
        0x0104,
        (
            '#0040150877V#035F……呼，艾丝蒂尔君。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040150878V不要这么看待我嘛。\n',
            '我会很困扰的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x14, 0x17, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010150879V#007F……真是不知反省呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_DDF(): pass

    label('loc_DDF')

    ChrTalk(
        0x0008,
        (
            '#1340150880V迪拜恩教区长是一位\n',
            '严于律己的人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1340150881V在劝诫他人的同时，\n',
            '也不断地反省自己。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1340150882V现在的年轻人\n',
            '都应该以他为榜样啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1340150883V我这样说是不是要求太高了呢。\n',
            '呵～呵～呵。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0EA9')
    def lambda_0EA9():
        ChrTurnDirection(0x0104, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0104, 0x0001, lambda_0EA9)

    ChrTurnDirection(0x0101, 0x0008, 400)

    ChrTalk(
        0x0101,
        (
            '#0010150884V#506F……呵～呵～呵。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1340150885V不过嘛， \n',
            '人们首先要严格要求自己，\n',
            '才能不断地进步。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0000, 0)

    ChrTalk(
        0x0008,
        (
            '#1340150886V你们从洛连特一路赶来，\n',
            '真是辛苦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1340150887V空之女神爱德丝啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1340150888V请赐予他们护佑……\n',
            '并且给予他们指引……',
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
            '任务【送亲笔信】',
            (TxtCtl.SetColor, 0x0),
            '完成！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrDirection(0x0008, 180, 0)
    EventEnd(0x00)
    TalkEnd(0x0008)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
