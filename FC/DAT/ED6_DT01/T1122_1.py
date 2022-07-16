import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T1122_1_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T1122_1 ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'T1122.x'
    header.mapIndex       = 1
    header.bgm            = 11
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x10D0
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
    OP_4A(0x000C, 255)
    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))
    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))
    OP_28(0x0011, 0x04, 0x04)
    OP_28(0x0011, 0x04, 0x02)
    OP_28(0x0011, 0x04, 0x08)
    OP_28(0x0011, 0x01, 0x0001)
    OP_28(0x0011, 0x01, 0x0002)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_101',
    )

    Fade(1000)
    SetChrPos(0x0101, 6800, 0, 6600, 90)
    SetChrPos(0x0102, 6600, 0, 5600, 90)

    If(
        (
            (Expr.Eval, "OP_42(0x0002)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Ez,
            Expr.Return,
        ),
        'loc_DE',
    )

    SetChrPos(0x0103, 5400, 0, 6400, 90)

    def _loc_DE(): pass

    label('loc_DE')

    If(
        (
            (Expr.Eval, "OP_42(0x0003)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Ez,
            Expr.Return,
        ),
        'loc_FE',
    )

    SetChrPos(0x0104, 5200, 0, 5400, 90)

    def _loc_FE(): pass

    label('loc_FE')

    Jump('loc_168')

    def _loc_101(): pass

    label('loc_101')

    Fade(1000)
    SetChrPos(0x0101, 10200, 0, 5800, 315)
    SetChrPos(0x0102, 9500, 0, 4800, 0)

    If(
        (
            (Expr.Eval, "OP_42(0x0002)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Ez,
            Expr.Return,
        ),
        'loc_148',
    )

    SetChrPos(0x0103, 10400, 0, 4200, 0)

    def _loc_148(): pass

    label('loc_148')

    If(
        (
            (Expr.Eval, "OP_42(0x0003)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Ez,
            Expr.Return,
        ),
        'loc_168',
    )

    SetChrPos(0x0104, 9500, 0, 3600, 0)

    def _loc_168(): pass

    label('loc_168')

    OP_69(0x0101, 0)
    ChrTurnDirection(0x000C, 0x0101, 0)
    OP_0D()

    ChrTalk(
        0x000C,
        (
            '#1360150935V想买点什么东西吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#1360150936V我店里的药都是很有效的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010150937V#000F是这样的，\n',
            '我们是看了公告板而来的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010150938V这么说，\n',
            '您就是思潘斯老爷爷吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#1360150939V哦，你们是游击士对吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#1360150940V我一直在等着你们呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020150941V#010F简而言之，\n',
            '就是寻找『熊刺草』的生长地带对吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2AE',
    )

    ChrTurnDirection(0x000C, 0x0102, 400)

    def _loc_2AE(): pass

    label('loc_2AE')

    ChrTalk(
        0x000C,
        (
            '#1360150942V『熊刺草』这种药草\n',
            '在这周边的地域\n',
            '好像是找不到的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#1360150943V之前都是拜托别人\n',
            '从洛连特帮我带过来的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#1360150944V不久前，\n',
            '豪尔斯教区长拜托我帮他调配一种新药。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#1360150945V今后会需要\n',
            '大量的这种药草来制药。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#1360150946V所以，\n',
            '我想事先找一些储备起来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0050, 4, 0x284)),
            (Expr.TestScenaFlags, ScenaFlag(0x0050, 5, 0x285)),
            Expr.Or,
            (Expr.TestScenaFlags, ScenaFlag(0x0050, 6, 0x286)),
            Expr.Or,
            (Expr.TestScenaFlags, ScenaFlag(0x0050, 7, 0x287)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_425',
    )

    ChrTalk(
        0x0101,
        (
            '#0010150947V#505F嗯～是『熊刺草』啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010150948V我记得在洛连特的\n',
            '神秘森林里有很多这种草。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_46D')

    def _loc_425(): pass

    label('loc_425')

    ChrTalk(
        0x0101,
        (
            '#0010150949V#505F嗯～是『熊刺草』啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010150950V在这附近\n',
            '确实没有见过呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_46D(): pass

    label('loc_46D')

    ChrTurnDirection(0x000C, 0x0101, 400)

    ChrTalk(
        0x000C,
        (
            '#1360150951V『熊刺草』这种药草\n',
            '喜欢生长在潮湿的地方。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#1360150952V我想在柏斯那些潮湿的地方\n',
            '一定也有生长。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010150953V#007F呼～\n',
            '又要到湿漉漉的地方去找啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x0002)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5B3',
    )

    ChrTalk(
        0x0103,
        (
            '#0030150954V#020F这种调查任务也是\n',
            '游击士很重要的工作之一哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030150955V把它当成一次学习的机会好好加油吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0103, 400)

    ChrTalk(
        0x0101,
        (
            '#0010150956V#505F唔，也只有这样了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5B3(): pass

    label('loc_5B3')

    ChrTalk(
        0x0102,
        (
            '#0020150957V#010F那么，\n',
            '我们一有消息就来通知您。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x000C, 400)

    ChrTalk(
        0x000C,
        (
            '#1360150958V好的，好的，拜托你们了。\n',
            '路上小心哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x00)
    OP_4B(0x000C, 255)

    Return()

# id: 0x0001 offset: 0x624
@scena.Code('Init')
def Init():
    ClearMapFlags(0x00000001)
    EventBegin(0x00)
    OP_4A(0x000C, 255)
    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))
    OP_28(0x0011, 0x04, 0x10)
    OP_28(0x0011, 0x04, 0x04)
    OP_28(0x0011, 0x04, 0x02)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_6B2',
    )

    Fade(1000)
    SetChrPos(0x0101, 6800, 0, 6600, 90)
    SetChrPos(0x0102, 6600, 0, 5600, 90)

    If(
        (
            (Expr.Eval, "OP_42(0x0002)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Ez,
            Expr.Return,
        ),
        'loc_68F',
    )

    SetChrPos(0x0103, 5400, 0, 6400, 90)

    def _loc_68F(): pass

    label('loc_68F')

    If(
        (
            (Expr.Eval, "OP_42(0x0003)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Ez,
            Expr.Return,
        ),
        'loc_6AF',
    )

    SetChrPos(0x0104, 5200, 0, 5400, 90)

    def _loc_6AF(): pass

    label('loc_6AF')

    Jump('loc_719')

    def _loc_6B2(): pass

    label('loc_6B2')

    Fade(1000)
    SetChrPos(0x0101, 10200, 0, 5800, 315)
    SetChrPos(0x0102, 9500, 0, 4800, 0)

    If(
        (
            (Expr.Eval, "OP_42(0x0002)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Ez,
            Expr.Return,
        ),
        'loc_6F9',
    )

    SetChrPos(0x0103, 10400, 0, 4200, 0)

    def _loc_6F9(): pass

    label('loc_6F9')

    If(
        (
            (Expr.Eval, "OP_42(0x0003)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Ez,
            Expr.Return,
        ),
        'loc_719',
    )

    SetChrPos(0x0104, 9500, 0, 3600, 0)

    def _loc_719(): pass

    label('loc_719')

    OP_69(0x0101, 0)
    ChrTurnDirection(0x000C, 0x0101, 0)
    OP_0D()

    ChrTalk(
        0x000C,
        (
            '#1360150935V想买点什么东西吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#1360150936V我店里的药都是很有效的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010150937V#000F是这样的，\n',
            '我们是看了公告板而来的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010150938V这么说，\n',
            '您就是思潘斯老爷爷吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#1360150939V哦，你们是游击士对吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#1360150940V我一直在等着你们呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020150941V#010F简而言之，\n',
            '就是寻找『熊刺草』的生长地带对吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_85F',
    )

    ChrTurnDirection(0x000C, 0x0102, 400)

    def _loc_85F(): pass

    label('loc_85F')

    ChrTalk(
        0x000C,
        (
            '#1360150942V『熊刺草』这种药草\n',
            '在这周边的地域\n',
            '好像是找不到的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#1360150943V之前都是拜托别人\n',
            '从洛连特帮我带过来的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#1360150944V不久前，\n',
            '豪尔斯教区长拜托我帮他调配一种新药。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#1360150945V今后会需要\n',
            '大量的这种药草来制药。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_29(0x0011, 0x01, 0x0004)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_A79',
    )

    OP_28(0x0011, 0x01, 0x0020)
    OP_28(0x0011, 0x01, 0x0040)
    OP_62(0x0101, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010150970V#505F咦？对了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010150971V#000F我们最近不是\n',
            '找到过『熊刺草』的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020150972V#010F嗯，是在迷雾峡谷里发现的。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#1360150973V是真的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0A18')
    def lambda_0A18():
        ChrTurnDirection(0x0101, 0x000C, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0A18)

    ChrTurnDirection(0x0102, 0x000C, 400)

    ChrTalk(
        0x0102,
        (
            '#0020150974V#010F数量虽然不是很多……\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020150975V不过用来配药也应该足够了。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B75')

    def _loc_A79(): pass

    label('loc_A79')

    OP_28(0x0011, 0x01, 0x0010)

    ChrTalk(
        0x0101,
        (
            '#0010150976V#001F嘿嘿，\n',
            '这样的话就没问题啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010150977V『熊刺草』这种药草\n',
            '在柏斯地区也有生长哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000C, 0x0101, 400)

    ChrTalk(
        0x000C,
        (
            '#1360150973V是真的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020150979V#010F在迷雾峡谷就有。\n',
            '我们亲眼见到了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020150980V数量虽然不是很多……\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020150975V不过用来配药也应该足够了。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_B75(): pass

    label('loc_B75')

    ChrTurnDirection(0x000C, 0x0102, 400)

    ChrTalk(
        0x000C,
        (
            '#1360150982V那真是太好了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#1360150983V果然……\n',
            '『熊刺草』喜爱潮湿的生长环境。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#1360150984V迷雾峡谷\n',
            '正是这样的地方呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#1360150985V真是太感谢你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#1360150986V这下我就可以放心地\n',
            '进行新药的调配了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010150987V#006F嗯⊙',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010150988V那么请加油哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020150989V#010F那么我们就告辞了。',
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
            '任务【调查『熊刺草』】',
            (TxtCtl.SetColor, 0x0),
            '完成！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    EventEnd(0x00)
    OP_4B(0x000C, 255)

    Return()

# id: 0x0002 offset: 0xCEE
@scena.Code('ReInit')
def ReInit():
    ClearMapFlags(0x00000001)
    EventBegin(0x00)
    OP_4A(0x000C, 255)
    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))
    OP_28(0x0011, 0x04, 0x10)
    OP_28(0x0011, 0x01, 0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_D78',
    )

    Fade(1000)
    SetChrPos(0x0101, 6800, 0, 6600, 90)
    SetChrPos(0x0102, 6600, 0, 5600, 90)

    If(
        (
            (Expr.Eval, "OP_42(0x0002)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Ez,
            Expr.Return,
        ),
        'loc_D55',
    )

    SetChrPos(0x0103, 5400, 0, 6400, 90)

    def _loc_D55(): pass

    label('loc_D55')

    If(
        (
            (Expr.Eval, "OP_42(0x0003)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Ez,
            Expr.Return,
        ),
        'loc_D75',
    )

    SetChrPos(0x0104, 5200, 0, 5400, 90)

    def _loc_D75(): pass

    label('loc_D75')

    Jump('loc_DDF')

    def _loc_D78(): pass

    label('loc_D78')

    Fade(1000)
    SetChrPos(0x0101, 10200, 0, 5800, 315)
    SetChrPos(0x0102, 9500, 0, 4800, 0)

    If(
        (
            (Expr.Eval, "OP_42(0x0002)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Ez,
            Expr.Return,
        ),
        'loc_DBF',
    )

    SetChrPos(0x0103, 10400, 0, 4200, 0)

    def _loc_DBF(): pass

    label('loc_DBF')

    If(
        (
            (Expr.Eval, "OP_42(0x0003)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Ez,
            Expr.Return,
        ),
        'loc_DDF',
    )

    SetChrPos(0x0104, 9500, 0, 3600, 0)

    def _loc_DDF(): pass

    label('loc_DDF')

    OP_69(0x0101, 0)
    ChrTurnDirection(0x000C, 0x0101, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010151060V#508F思潘斯老爷爷，您好啊⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#1360151061V哦，\n',
            '这不是游击士协会的小姑娘吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#1360151062V调查方面有什么进展吗？\n',
            '说来给我听听。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010151063V#001F嗯⊙非常顺利哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010151064V在柏斯周围果然也有\n',
            '『熊刺草』生长的地方呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020150979V#010F在迷雾峡谷就有生长。\n',
            '我们亲眼见到了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020150980V数量虽然不是很多……\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020150975V不过用来配药也应该足够了。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_F58',
    )

    ChrTurnDirection(0x000C, 0x0102, 400)

    def _loc_F58(): pass

    label('loc_F58')

    ChrTalk(
        0x000C,
        (
            '#1360150982V那真是太好了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#1360150983V果然……\n',
            '『熊刺草』喜爱潮湿的生长环境。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#1360150984V迷雾峡谷\n',
            '正是这样的地方呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#1360150985V真是太感谢你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#1360150986V这下我就可以放心地\n',
            '进行新药的调配了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010150987V#006F嗯⊙',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010150988V那么请加油哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020151075V#010F那么我们就告辞了。',
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
            '任务【调查『熊刺草』】',
            (TxtCtl.SetColor, 0x0),
            '完成！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    EventEnd(0x00)
    OP_4B(0x000C, 255)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
