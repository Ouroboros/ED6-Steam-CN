import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T1111_1_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T1111_1 ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'C0403.x'
    header.mapIndex       = 1
    header.bgm            = 10
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 'ED6_DT21/T1111_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x3761
@scena.StringTable('StringTable')
def StringTable():
    return stringTable

# id: 0x10000 offset: 0x64
@scena.EntryPoint('EntryPoint')
def EntryPoint():
    return (
        ScenaEntryPoint(
            dword_00        = 0x00000000,
            dword_04        = 0x00000000,
            dword_08        = 0x00001770,
            word_0C         = 0x0004,
            word_0E         = 0x0000,
            dword_10        = 0,
            dword_14        = 9500,
            dword_18        = -10000,
            dword_1C        = 0,
            dword_20        = 0,
            dword_24        = 0,
            dword_28        = 2800,
            dword_2C        = 262,
            word_30         = 45,
            word_32         = 0,
            word_34         = 360,
            word_36         = 0,
            word_38         = 0,
            word_3A         = 0,
            preInitScena    = 0x0000,
            preInitFunction = 0x0000,
            initScena       = 0x0000,
            initFunction    = 0x0001,
        ),
    )

# id: 0x10001 offset: 0xA8
@scena.ChipData('ChipData')
def ChipData():
    return [
        # (ch, cp)
    ]

# id: 0x10002 offset: 0xA8
@scena.NpcData('NpcData')
def NpcData():
    return (
    )

# id: 0x10003 offset: 0xA8
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0xA8
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0xA8
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0xA8
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.PushValueByIndex, 0x13),
            (Expr.PushLong, 0x381),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_B5',
    )

    Return()

    def _loc_B5(): pass

    label('loc_B5')

    If(
        (
            (Expr.Eval, "OP_29(0x0079, 0x00, 0x10)"),
            (Expr.Eval, "OP_29(0x0079, 0x00, 0x40)"),
            Expr.Or,
            Expr.Return,
        ),
        'loc_C7',
    )

    Return()

    def _loc_C7(): pass

    label('loc_C7')

    SetMapFlags(0x00000080)
    OP_C0(0x01, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000)
    Sleep(30)

    If(
        (
            (Expr.Eval, "OP_CD(0x0008)"),
            Expr.Return,
        ),
        'loc_102',
    )

    Call(1, 0x0001)

    Jump('loc_16D')

    def _loc_102(): pass

    label('loc_102')

    If(
        (
            (Expr.Eval, "OP_CD(0x0009)"),
            Expr.Return,
        ),
        'loc_111',
    )

    Call(1, 0x0002)

    Jump('loc_16D')

    def _loc_111(): pass

    label('loc_111')

    If(
        (
            (Expr.Eval, "OP_CD(0x000B)"),
            Expr.Return,
        ),
        'loc_120',
    )

    Call(1, 0x0003)

    Jump('loc_16D')

    def _loc_120(): pass

    label('loc_120')

    If(
        (
            (Expr.Eval, "OP_CD(0x000C)"),
            Expr.Return,
        ),
        'loc_12F',
    )

    Call(1, 0x0004)

    Jump('loc_16D')

    def _loc_12F(): pass

    label('loc_12F')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '附近没有人可以确认照片。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    def _loc_16D(): pass

    label('loc_16D')

    OP_0D()
    ClearMapFlags(0x00000080)

    Return()

# id: 0x0001 offset: 0x174
@scena.Code('Init')
def Init():
    EventBegin(0x00)
    Fade(1000)
    SetChrSubChip(0x0008, 1)
    SetChrPos(0x0101, -119000, 0, 68680, 270)

    If(
        (
            (Expr.Eval, "OP_CB(0xF7)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1D4',
    )

    SetChrPos(0x00F8, -118380, 0, 69420, 270)
    SetChrPos(0x00F7, -117250, 0, 68490, 270)
    SetChrPos(0x00F9, -118000, 0, 67990, 270)

    Jump('loc_28D')

    def _loc_1D4(): pass

    label('loc_1D4')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_217',
    )

    SetChrPos(0x00F7, -118380, 0, 69420, 270)
    SetChrPos(0x00F8, -117250, 0, 68490, 270)
    SetChrPos(0x00F9, -118000, 0, 67990, 270)

    Jump('loc_28D')

    def _loc_217(): pass

    label('loc_217')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_25A',
    )

    SetChrPos(0x00F7, -118380, 0, 69420, 270)
    SetChrPos(0x00F9, -117250, 0, 68490, 270)
    SetChrPos(0x00F8, -118000, 0, 67990, 270)

    Jump('loc_28D')

    def _loc_25A(): pass

    label('loc_25A')

    SetChrPos(0x00F7, -118380, 0, 69420, 270)
    SetChrPos(0x00F8, -117250, 0, 68490, 270)
    SetChrPos(0x00F9, -118000, 0, 67990, 270)

    def _loc_28D(): pass

    label('loc_28D')

    OP_6D(-119770, 0, 69530, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    OP_0D()

    If(
        (
            (Expr.Eval, "OP_29(0x0079, 0x01, 0x0004)"),
            Expr.Return,
        ),
        'loc_4AC',
    )

    ChrTalk(
        0x0008,
        (
            '#0360490646V#612F那么，各位……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360490647V那张照片……\n',
            '已经给莉拉看过了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_29(0x0079, 0x01, 0x0008)"),
            Expr.Return,
        ),
        'loc_430',
    )

    ChrTalk(
        0x0101,
        (
            '#0010490648V#1011F啊，嗯。\n',
            '给她看过了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0360490638V#612F那么……\n',
            '她有说什么吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010490639V#1015F不，她看起来虽然\n',
            '感到很吃惊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010490640V但是，她也只是吃惊一下，\n',
            '却什么都没说呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010490641V#1002F看来果然是\n',
            '在隐瞒着什么。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Call(1, 0x0005)

    Jump('loc_4A9')

    def _loc_430(): pass

    label('loc_430')

    ChrTalk(
        0x0101,
        (
            '#0010490653V#1002F不，还没有。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0360490654V#612F那就先把照片给\n',
            '莉拉看吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360490655V我想一定能\n',
            '得到线索的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4A9(): pass

    label('loc_4A9')

    Jump('loc_81B')

    def _loc_4AC(): pass

    label('loc_4AC')

    OP_62(0x0008, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#0360490629V#613F啊，这是……！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360490630V这张照片你们到底是从哪里得到的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010490631V#1015F嗯，其实是这样……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '艾丝蒂尔等人说明了\n',
            '关于寻找科尔娜在『百日战役』中失踪的侄女的事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    ChrTalk(
        0x0008,
        (
            '#0360490632V#618F是吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360490633V到了现在还有这样的事啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010490634V#1002F你有什么印象吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0360490635V#615F嗯……有点。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360490636V#612F那个，这张照片……\n',
            '已经给莉拉看过了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_29(0x0079, 0x01, 0x0008)"),
            Expr.Return,
        ),
        'loc_784',
    )

    ChrTalk(
        0x0101,
        (
            '#0010490637V#1011F啊，嗯。\n',
            '刚才给她看过了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0360490638V#612F那么……\n',
            '她有说什么吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010490639V#1015F不，她看起来虽然\n',
            '相当吃惊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010490640V但是，她也只是吃惊一下，\n',
            '什么都没说呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010490641V#1002F看来果然是\n',
            '在隐瞒着什么。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x0079, 0x01, 0x0010)
    Call(1, 0x0005)

    Jump('loc_81B')

    def _loc_784(): pass

    label('loc_784')

    ChrTalk(
        0x0101,
        (
            '#0010490642V#1011F莉拉小姐？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010490643V#1000F不，还没有。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0360490644V#612F那就先给她\n',
            '看看吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360490645V我想大概能\n',
            '得到线索的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x0079, 0x01, 0x0004)

    def _loc_81B(): pass

    label('loc_81B')

    SetChrSubChip(0x0008, 0)
    EventEnd(0x04)

    Return()

# id: 0x0002 offset: 0x823
@scena.Code('ReInit')
def ReInit():
    TalkBegin(0x0009)

    If(
        (
            (Expr.Eval, "OP_29(0x0079, 0x01, 0x0008)"),
            Expr.Return,
        ),
        'loc_888',
    )

    ChrTalk(
        0x0009,
        (
            '#0370490675V#620F现在我正在打扫，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0370490676V实在抱歉，\n',
            '有事的话请等会再说。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C08')

    def _loc_888(): pass

    label('loc_888')

    OP_62(0x0009, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0009,
        (
            '#0370490656V#628F…………！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0370490657V这张照片……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010490631V#1015F嗯，其实是这样……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '艾丝蒂尔等人说明了\n',
            '关于寻找科尔娜在『百日战役』中失踪的侄女的事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    ChrTalk(
        0x0009,
        (
            '#0370490659V#627F…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010490660V#1002F你有印象吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0009, 0x0101, 400)

    ChrTalk(
        0x0009,
        (
            '#0370490661V#624F不……\n',
            '没什么。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010490662V#1002F……真的？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010490663V你好像看上去\n',
            '很吃惊的样子……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_29(0x0079, 0x01, 0x0004)"),
            Expr.Return,
        ),
        'loc_B80',
    )

    ChrTalk(
        0x0009,
        (
            '#0370490664V#620F嗯，和我的一个\n',
            '熟人长得很像……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0370490665V所以我就\n',
            '愣了一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010490666V#1015F是，是吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010490667V唔，真奇怪。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010490668V梅贝尔市长明明说\n',
            '问了莉拉小姐就会明白的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0370490669V#620F啊，是吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0370490670V那好我先要\n',
            '告辞了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0370490671V因为还有工作\n',
            '等着我去做。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C02')

    def _loc_B80(): pass

    label('loc_B80')

    ChrTalk(
        0x0009,
        (
            '#0370490664V#620F嗯，和我的一个\n',
            '熟人长得很像……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0370490673V所以我就\n',
            '愣了一下。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0370490674V那我就先告辞了。\n',
            '我还有工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_C02(): pass

    label('loc_C02')

    OP_28(0x0079, 0x01, 0x0008)

    def _loc_C08(): pass

    label('loc_C08')

    TalkEnd(0x0009)

    Return()

# id: 0x0003 offset: 0xC0C
@scena.Code('func_03_C0C')
def func_03_C0C():
    TalkBegin(0x000B)

    ChrTalk(
        0x000B,
        (
            '#3760490619V哇～好可爱的女孩子～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#3760490620V和我小时候可能很像！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x000B)

    Return()

# id: 0x0004 offset: 0xC5F
@scena.Code('func_04_C5F')
def func_04_C5F():
    TalkBegin(0x000C)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_CD4',
    )

    ChrTalk(
        0x000C,
        (
            '#1140490624V因为我记得曾经在老爷的\n',
            '书房见过这名少女的照片。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#1140490625V到底是谁的\n',
            '照片呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_DE8')

    def _loc_CD4(): pass

    label('loc_CD4')

    ChrTalk(
        0x000C,
        (
            '#1140490621V哎呀，这张照片……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010490622V#1004F你有印象吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000C, 0x0101, 400)

    ChrTalk(
        0x000C,
        (
            '#1140490623V虽然记\n',
            '不太清楚……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#1140490624V因为我记得曾经在老爷的\n',
            '书房见过这名少女的照片。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#1140490625V到底是谁的\n',
            '照片呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#1140490626V不过看到的时候\n',
            '我也觉得很不可思议。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0005)

    def _loc_DE8(): pass

    label('loc_DE8')

    TalkEnd(0x000C)

    Return()

# id: 0x0005 offset: 0xDEC
@scena.Code('func_05_DEC')
def func_05_DEC():
    SetChrSubChip(0x0008, 0)

    ChrTalk(
        0x0008,
        (
            '#0360490677V#615F是吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360490678V呼，看来还是要\n',
            '从我嘴里说出来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    OP_22(0x0026, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010490679V#1011F那个，我还是\n',
            '不大明白……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010490680V……到底是怎么回事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_59()
    OP_20(0x000003E8)
    Sleep(400)

    ChrTalk(
        0x0008,
        (
            '#0360490681V#618F那张照片上的少女……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360490682V……正是莉拉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_21()
    OP_1D(0x53)
    Sleep(400)

    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010490683V#1004F咦咦！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_F6D',
    )

    ChrTalk(
        0x0105,
        (
            '#0060490684V#044F啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_F6D(): pass

    label('loc_F6D')

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_FA0',
    )

    ChrTalk(
        0x0107,
        (
            '#0070490685V#064F真、真的吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_FA0(): pass

    label('loc_FA0')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1000',
    )

    ChrTalk(
        0x0104,
        (
            '#0040490686V#033F这……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040490687V怎么说……\n',
            '真是个具有震撼性的新发现呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1000(): pass

    label('loc_1000')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1037',
    )

    ChrTalk(
        0x0108,
        (
            '#0080490688V#073F这可真让人吃惊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1037(): pass

    label('loc_1037')

    If(
        (
            (Expr.Eval, "OP_42(0x08)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1073',
    )

    ChrTalk(
        0x0109,
        (
            '#0180490689V#1064F啊，女神也会吓一跳吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1073(): pass

    label('loc_1073')

    ChrTalk(
        0x0101,
        (
            '#0010490690V#1004F那、那个……\n',
            '你确定？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrSubChip(0x0008, 1)

    ChrTalk(
        0x0008,
        (
            '#0360490691V#612F嗯，我敢肯定。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360490692V#615F莉拉是在十年前的\n',
            '某一天来到我家的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360490693V正是柏斯被『百日战役』的\n',
            '战火席卷的那一天。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010490694V#1026F原、原来是这样……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0360490695V#618F从市民避难的地方回来的父亲\n',
            '带来了一名少女。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360490696V父亲说是受到了\n',
            '陌生人的托付……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360490697V……那个女孩子就是莉拉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1265',
    )

    ChrTalk(
        0x0103,
        (
            '#0030490698V#022F和科尔娜女士的证词有\n',
            '很多相符的地方。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030490699V我觉得这很可信。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1404')

    def _loc_1265(): pass

    label('loc_1265')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_12CC',
    )

    ChrTalk(
        0x0106,
        (
            '#0050490700V#050F和委托人的证词有\n',
            '很多相符的地方。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050490701V我觉得这很可信。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1404')

    def _loc_12CC(): pass

    label('loc_12CC')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1338',
    )

    ChrTalk(
        0x0108,
        (
            '#0080490702V#074F和委托人的证词有\n',
            '很多相符的地方。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080490703V#072F我觉得这很可信。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1404')

    def _loc_1338(): pass

    label('loc_1338')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_139F',
    )

    ChrTalk(
        0x0104,
        (
            '#0040490704V#030F和委托人的证词有\n',
            '很多相符的地方。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040490705V我觉得这很可信。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1404')

    def _loc_139F(): pass

    label('loc_139F')

    If(
        (
            (Expr.Eval, "OP_42(0x08)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1404',
    )

    ChrTalk(
        0x0109,
        (
            '#0180490706V#1063F和委托人的证词有\n',
            '很多相符的地方。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180490707V我觉得这很可信。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1404(): pass

    label('loc_1404')

    ChrTalk(
        0x0101,
        (
            '#0010490708V#1015F不过……\n',
            '名字好像不一样。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010490709V科尔娜女士的侄女\n',
            '名字应该叫蕾妮。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0360490710V#613F蕾妮……？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360490711V这就是莉拉原来的名字？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010490712V#1002F嗯……\n',
            '委托人是这么说的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010490713V莫非梅贝尔市长\n',
            '也不知道莉拉小姐的本名？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0360490714V#618F嗯，很遗憾……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_15B1',
    )

    ChrTalk(
        0x0106,
        (
            '#0050490715V#052F她本人没说过自己的原名吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050490716V照片上的年龄还没小到\n',
            '连名字也说不清的程度吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_17A3')

    def _loc_15B1(): pass

    label('loc_15B1')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_162E',
    )

    ChrTalk(
        0x0104,
        (
            '#0040490717V#033F她本人没说过自己的原名吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040490718V照片上的年龄还没小到\n',
            '连名字也说不清的程度吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_17A3')

    def _loc_162E(): pass

    label('loc_162E')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_16AB',
    )

    ChrTalk(
        0x0108,
        (
            '#0080490719V#073F她本人没说过自己的原名吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080490720V照片上的年龄还没小到\n',
            '连名字也说不清的程度吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_17A3')

    def _loc_16AB(): pass

    label('loc_16AB')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1728',
    )

    ChrTalk(
        0x0103,
        (
            '#0030490721V#023F她本人没说过自己的原名吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030490722V照片上的年龄还没小到\n',
            '连名字也说不清的程度吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_17A3')

    def _loc_1728(): pass

    label('loc_1728')

    If(
        (
            (Expr.Eval, "OP_42(0x08)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_17A3',
    )

    ChrTalk(
        0x0109,
        (
            '#0180490723V#1064F她本人没说过自己的原名吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180490724V照片上的年龄还没小到\n',
            '连名字也说不清的程度吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_17A3(): pass

    label('loc_17A3')

    ChrTalk(
        0x0008,
        (
            '#0360490725V#618F嗯，她要是说出\n',
            '自己的名字当然好……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360490726V不过她来我家的时候\n',
            '并不开口说话。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360490727V怎么说好呢……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360490728V……对，就好像是\n',
            '忘了应该怎么说话一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010490729V#1020F什、什么意思？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x08)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1931',
    )

    ChrTalk(
        0x0109,
        (
            '#0180490730V#1067F大概是暂时性\n',
            '失语症吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180490731V是一种过度的精神负担\n',
            '所引发的症状……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180490732V对那么小的孩子来说，\n',
            '那段时间真的是太残酷了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1C2D')

    def _loc_1931(): pass

    label('loc_1931')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_19F8',
    )

    ChrTalk(
        0x0108,
        (
            '#0080490733V#072F可能是因为精神打击\n',
            '而引发的暂时性失语症。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080490734V好像过度残酷的经历\n',
            '就会造成这种情况……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080490735V真是的，这真是令人感叹啊。\n',
            '她当初应该受了不少苦吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1C2D')

    def _loc_19F8(): pass

    label('loc_19F8')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1ABD',
    )

    ChrTalk(
        0x0104,
        (
            '#0041050032V#032F可能是因为精神打击\n',
            '而引发的暂时性失语症。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040490736V我听说过因为在战争中\n',
            '经历了过于残酷的事而发病的病例。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040490737V真可怜……\n',
            '她当初应该受了不少苦吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1C2D')

    def _loc_1ABD(): pass

    label('loc_1ABD')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1B72',
    )

    ChrTalk(
        0x0103,
        (
            '#0030490738V#522F可能是因为受打击\n',
            '而引发的暂时性失语症。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030490739V好像过度残酷的经历\n',
            '就会造成这种情况……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030490740V真可怜……\n',
            '她当初应该受了不少苦吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1C2D')

    def _loc_1B72(): pass

    label('loc_1B72')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1C2D',
    )

    ChrTalk(
        0x0106,
        (
            '#0050490741V#053F可能是因为受打击\n',
            '而引发的暂时性失语症。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050490742V好像过度残酷的经历\n',
            '就会造成这种情况……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050490743V#552F真是很可怜啊。\n',
            '她当初应该受了不少苦吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1C2D(): pass

    label('loc_1C2D')

    ChrTalk(
        0x0008,
        (
            '#0360490744V#615F嗯，她的内心一定\n',
            '受过很深的伤吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360490745V虽然大家都努力过，\n',
            '不过她还是没打开自己的心扉……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360490746V……所以，我们也\n',
            '不知道莉拉的本名。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010490747V#1002F那、那么……\n',
            '莉拉小姐现在的名字呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0360490748V#612F是父亲给她起的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360490749V因为没有名字\n',
            '是很不方便的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1DCD',
    )

    ChrTalk(
        0x0103,
        (
            '#0030490750V#026F原来如此，明白了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030490751V那样的话，\n',
            '接下来只有去问问她本人了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1F78')

    def _loc_1DCD(): pass

    label('loc_1DCD')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1E3A',
    )

    ChrTalk(
        0x0106,
        (
            '#0050490752V#053F原来如此，明白了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050490753V那样的话，\n',
            '接下来只有去问问她本人了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1F78')

    def _loc_1E3A(): pass

    label('loc_1E3A')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1EA7',
    )

    ChrTalk(
        0x0108,
        (
            '#0080490754V#074F原来如此，明白了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080490755V那样的话，\n',
            '接下来只有去问问她本人了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1F78')

    def _loc_1EA7(): pass

    label('loc_1EA7')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1F14',
    )

    ChrTalk(
        0x0104,
        (
            '#0040490756V#032F原来如此，明白了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040490757V那样的话，\n',
            '接下来只有去问问她本人了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1F78')

    def _loc_1F14(): pass

    label('loc_1F14')

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1F78',
    )

    ChrTalk(
        0x0105,
        (
            '#0060490758V#042F原来如此，明白了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060490759V这样的话，\n',
            '只有去问问她本人了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1F78(): pass

    label('loc_1F78')

    ChrTalk(
        0x0008,
        (
            '#0360490760V#615F嗯，确实如此……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360490761V#612F总之，我先去\n',
            '把她叫来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    SetChrChipByIndex(0x0008, 0)
    ClearChrFlags(0x0008, 0x0010)
    ClearChrFlags(0x0008, 0x0004)
    SetChrPos(0x0008, -120720, 0, 66270, 135)
    SetChrPos(0x0101, -121860, 0, 65600, 90)

    If(
        (
            (Expr.Eval, "OP_CB(0xF7)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2048',
    )

    SetChrPos(0x00F8, -121860, 0, 64500, 90)
    SetChrPos(0x00F9, -122900, 0, 65080, 90)
    SetChrPos(0x00F7, -122900, 0, 66180, 90)

    Jump('loc_2101')

    def _loc_2048(): pass

    label('loc_2048')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_208B',
    )

    SetChrPos(0x00F7, -121860, 0, 64500, 90)
    SetChrPos(0x00F9, -122900, 0, 65080, 90)
    SetChrPos(0x00F8, -122900, 0, 66180, 90)

    Jump('loc_2101')

    def _loc_208B(): pass

    label('loc_208B')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_20CE',
    )

    SetChrPos(0x00F7, -121860, 0, 64500, 90)
    SetChrPos(0x00F8, -122900, 0, 65080, 90)
    SetChrPos(0x00F9, -122900, 0, 66180, 90)

    Jump('loc_2101')

    def _loc_20CE(): pass

    label('loc_20CE')

    SetChrPos(0x00F7, -121860, 0, 64500, 90)
    SetChrPos(0x00F8, -122900, 0, 65080, 90)
    SetChrPos(0x00F9, -122900, 0, 66180, 90)

    def _loc_2101(): pass

    label('loc_2101')

    OP_6D(-120720, 0, 66270, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    OP_4A(0x0008, 255)
    OP_67(0, 4710, -10000, 0)
    OP_6B(3000, 0)
    FadeIn(1000, 0)
    OP_0D()
    SetChrPos(0x000B, -118000, 0, 62730, 0)
    OP_9F(0x000B, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    SetChrFlags(0x000B, 0x0040)
    SetChrPos(0x0009, -118000, 0, 62730, 0)
    OP_9F(0x0009, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    SetChrFlags(0x0009, 0x0040)
    CreateThread(0x000B, 0x00, 0x01, 0x0007)
    CreateThread(0x0009, 0x00, 0x01, 0x0006)
    WaitForThreadExit(0x0009, 0x0000)

    ChrTalk(
        0x000B,
        (
            '#3760490762V我把她带来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x000B, 400)

    ChrTalk(
        0x0008,
        (
            '#0360490763V#610F#5P谢谢你，萨拉。\n',
            '麻烦你先出去下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#3760490764V是，失陪了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x000B, 90, 400)
    OP_8E(0x000B, -118000, 0, 64530, 2000, 0x00)

    @scena.Lambda('lambda_2240')
    def lambda_2240():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x000003E8)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_2240)

    OP_8E(0x000B, -118000, 0, 62730, 2000, 0x00)
    SetChrFlags(0x000B, 0x0080)

    @scena.Lambda('lambda_226B')
    def lambda_226B():
        ChrTurnDirection(0x0008, 0x0009, 0)
        Yield()

        Jump('lambda_226B')

    DispatchAsync2(0x0008, 0x0001, lambda_226B)

    ChrTalk(
        0x0008,
        (
            '#0360490765V#612F#5P你到这边来，莉拉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_22A8')
    def lambda_22A8():
        OP_6D(-121200, 0, 66520, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_22A8)

    OP_8E(0x0009, -119080, 0, 66270, 2000, 0x00)
    ChrTurnDirection(0x0009, 0x0008, 400)
    TerminateThread(0x0008, 0x01)
    TerminateThread(0x0101, 0x01)

    ChrTalk(
        0x0009,
        (
            '#0370490766V#620F您有什么吩咐吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0360490767V#615F#5P那张照片……\n',
            '我也看过了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360490768V好久没像这样\n',
            '见到了一张令人怀念的脸。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360490769V#612F莉拉……\n',
            '那是你吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0370490770V#620F…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0360490771V#612F#5P你沉默的理由\n',
            '我很明白。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360490772V你很在意我\n',
            '父亲吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360490773V我知道你念及\n',
            '亡父的深厚恩情。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360490774V#615F但是莉拉……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360490775V我不希望这\n',
            '成为你人生的重担。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0370490776V#624F重担吗……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0360490777V#612F#5P嗯，你现在沉默不语\n',
            '正说明了这一点。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360490778V正是因为感到欠父亲的人情\n',
            '你才会这么做的吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0370490779V#627F我、我没……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0360490780V#615F#5P父亲以前经常说，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360490781V只要还在为过去所束缚，\n',
            '就决不可能开辟新的道路……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360490782V#612F莉拉，你已经为我家\n',
            '做了够多的事了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360490783V不必再一直\n',
            '陷在过去的影子里。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360490784V……你去见见科尔娜女士吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360490785V去见她，去取回\n',
            '属于你的人生。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0370490786V#620F…………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0370490787V小姐……\n',
            '我明白您的意思。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0370490788V#621F可是很遗憾……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0370490789V各位所寻找的蕾妮\n',
            '并不在这里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010290643V#1026F#1P咦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0360490791V#613F#5P……什么意思？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0370490792V#620F蕾妮在那场战争中\n',
            '和父母一起丧失了生命。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0370490793V现在她正在大地的\n',
            '某个角落安详地沉睡……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0370490794V……我相信着这一点，\n',
            '一直活到了今天。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0370490795V#625F不这么想的话，\n',
            '我就会感到很孤单……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0360490796V#618F#5P莉拉……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010490797V#1026F#1P莉拉小姐……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0360490798V#618F#5P是吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360490799V是这样的吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360490800V没想到你是一直怀抱着\n',
            '这样的心情走过来的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010490801V#1010F#1P…………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010490802V#1025F可是，莉拉小姐……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010490803V那样的谎言\n',
            '已经不需要了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0370490804V#620F…………！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010490805V#1000F#1P梅贝尔市长和萨拉小姐……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010490806V管家门特斯先生和\n',
            '超市里的人们……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010490807V大家都把莉拉\n',
            '当成是自己的亲人一样。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010490808V现在的莉拉小姐\n',
            '一点也不孤独。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0101, 400)

    ChrTalk(
        0x0008,
        (
            '#0360490809V#613F#5P艾丝蒂尔小姐……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2AA4',
    )

    ChrTalk(
        0x0103,
        (
            '#0030320335V#020F艾丝蒂尔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2AA4(): pass

    label('loc_2AA4')

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2AD3',
    )

    ChrTalk(
        0x0107,
        (
            '#0070490811V#060F嗯，没错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2AD3(): pass

    label('loc_2AD3')

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2B0D',
    )

    ChrTalk(
        0x0105,
        (
            '#0060490812V#047F我也……\n',
            '觉得是这样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2B0D(): pass

    label('loc_2B0D')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2B4B',
    )

    ChrTalk(
        0x0106,
        (
            '#0050490813V#051F啊啊……\n',
            '这家伙说得没错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2B4B(): pass

    label('loc_2B4B')

    If(
        (
            (Expr.Eval, "OP_42(0x08)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2B96',
    )

    ChrTalk(
        0x0109,
        (
            '#0180490814V#1060F人与人之间的羁绊\n',
            '比你想象的更为紧密。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2B96(): pass

    label('loc_2B96')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2C04',
    )

    ChrTalk(
        0x0108,
        (
            '#0080490815V#070F嗯，我也同意。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080490816V就凭这次案件调查中\n',
            '的亲身经历给我留下的印象。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2C04(): pass

    label('loc_2C04')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2C60',
    )

    ChrTalk(
        0x0104,
        (
            '#0040490817V#031F呵呵，是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040490818V至少我还是\n',
            '深深爱着莉拉你的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2C60(): pass

    label('loc_2C60')

    ChrTurnDirection(0x0008, 0x0009, 400)

    ChrTalk(
        0x0008,
        (
            '#0360490819V#612F#5P莉拉……\n',
            '你听见各位的话了吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360490820V#615F对我来说，你是\n',
            '家庭成员中的重要的一份子了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360490821V不，父亲去世之后\n',
            '你已经是我唯一的亲人了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360490822V#618F可你还说自己孤独……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360490823V以后请你不要再说\n',
            '这么悲伤的话了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0370490824V#627F小姐……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0360490825V#615F而且，莉拉……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360490826V为了忘却痛苦的事情\n',
            '而欺骗自己……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360490827V把自己囚禁在过去中的行为…\n',
            '这正是父亲所讨厌的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360490828V#612F请不要让父亲真心的教诲……\n',
            '付之东流。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360490829V莉拉……\n',
            '去见见科尔娜女士吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360490830V难道说……\n',
            '你是那种无视恩人教诲的\n',
            '不感恩之人？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0370490831V#627F……………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0370490832V#623F……明白了，我投降。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0370490833V唉，小姐你真是\n',
            '伶牙俐齿…………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0370490834V被这么一说，\n',
            '任何人都无法拒绝了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0360490835V#610F呵呵，这种激将法\n',
            '是谈判的基本功。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2FE7',
    )

    ChrTalk(
        0x0108,
        (
            '#0080490836V#070F嗯，看来\n',
            '已经有结果了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_30DB')

    def _loc_2FE7(): pass

    label('loc_2FE7')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3022',
    )

    ChrTalk(
        0x0106,
        (
            '#0050490837V#051F看来\n',
            '已经有结果了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_30DB')

    def _loc_3022(): pass

    label('loc_3022')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3063',
    )

    ChrTalk(
        0x0103,
        (
            '#0030490838V#027F呵呵，看来\n',
            '已经有结果了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_30DB')

    def _loc_3063(): pass

    label('loc_3063')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_30A2',
    )

    ChrTalk(
        0x0104,
        (
            '#0040490839V#031F嗯，看来\n',
            '已经有结果了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_30DB')

    def _loc_30A2(): pass

    label('loc_30A2')

    If(
        (
            (Expr.Eval, "OP_42(0x08)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_30DB',
    )

    ChrTalk(
        0x0109,
        (
            '#0180490840V#1060F看来已经\n',
            '有结果了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_30DB(): pass

    label('loc_30DB')

    ChrTalk(
        0x0101,
        (
            '#0010490841V#1007F呼，事情能圆满解决\n',
            '真是太好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0101, 400)

    ChrTalk(
        0x0008,
        (
            '#0360490842V#617F嗯，总算……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360490843V#611F那么，我们就\n',
            '马上去见她吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0370490844V#622F……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0008, 400)

    ChrTalk(
        0x0101,
        (
            '#0010490845V#1011F去见科尔娜女士……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010490846V……梅贝尔市长你亲自去？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3255',
    )

    ChrTalk(
        0x0106,
        (
            '#0050490847V#051F这倒没什么问题。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050490848V以代表父亲的名义一同出席，\n',
            '对方也应该会同意吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_342F')

    def _loc_3255(): pass

    label('loc_3255')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_32CA',
    )

    ChrTalk(
        0x0103,
        (
            '#0030490849V#020F这倒没什么问题。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030490850V以代表父亲的名义一同出席，\n',
            '对方也应该会同意吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_342F')

    def _loc_32CA(): pass

    label('loc_32CA')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3341',
    )

    ChrTalk(
        0x0108,
        (
            '#0080490851V#070F嗯，应该没问题的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080490852V以代表父亲的名义一同出席，\n',
            '对方也应该会同意吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_342F')

    def _loc_3341(): pass

    label('loc_3341')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_33BA',
    )

    ChrTalk(
        0x0104,
        (
            '#0040490853V#030F嗯，应该没任何问题。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040490854V以代表父亲的名义一同出席，\n',
            '对方也应该会同意吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_342F')

    def _loc_33BA(): pass

    label('loc_33BA')

    If(
        (
            (Expr.Eval, "OP_42(0x08)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_342F',
    )

    ChrTalk(
        0x0109,
        (
            '#0180490855V#1060F我觉得没什么问题。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180490856V以代表父亲的名义一同出席，\n',
            '对方也应该会同意吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_342F(): pass

    label('loc_342F')

    ChrTalk(
        0x0008,
        (
            '#0360490857V#611F呵呵，那就谢谢你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0009, 400)

    ChrTalk(
        0x0008,
        (
            '#0360490858V#610F莉拉，我们走。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0370490859V#621F……是。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0370490860V那么我陪您去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0360490861V#617F真是的，你在说些什么啊。\n',
            '是我陪你去。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360490862V快点，你走在我前面。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8E(0x0008, -119760, 0, 66290, 2000, 0x00)
    OP_8C(0x0009, 135, 400)

    @scena.Lambda('lambda_3542')
    def lambda_3542():
        OP_8E(0x0008, -119490, 0, 66180, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_3542)

    @scena.Lambda('lambda_355D')
    def lambda_355D():
        OP_8E(0x0009, -118590, 0, 65760, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_355D)

    WaitForThreadExit(0x0008, 0x0001)
    WaitForThreadExit(0x0009, 0x0001)
    OP_8C(0x0009, 270, 400)
    WaitForThreadExit(0x0009, 0x0000)
    OP_62(0x0009, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)

    ChrTalk(
        0x0009,
        (
            '#0370490863V#623F可、可是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010490864V#1001F哈哈，偶尔一次\n',
            '也无妨吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010490865V再说主角本来就是莉拉小姐。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0360490866V#611F呵呵，就是这样。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360490867V好，快点去吧。\n',
            '我等会儿会跟着你去的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0009, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)

    ChrTalk(
        0x0009,
        (
            '#0370490868V#626F小、小姐……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    OP_28(0x0079, 0x01, 0x0020)
    SetMapFlags(0x02000000)
    OP_A2(0x10F0)
    NewScene('ED6_DT21/T1131._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0006 offset: 0x36C8
@scena.Code('func_06_36C8')
def func_06_36C8():
    Sleep(1500)

    @scena.Lambda('lambda_36D3')
    def lambda_36D3():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x000003E8)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_36D3)

    OP_8E(0x00FE, -118000, 0, 64530, 2000, 0x00)
    OP_8E(0x00FE, -118370, 0, 65129, 2000, 0x00)
    ChrTurnDirection(0x00FE, 0x0008, 400)

    Return()

# id: 0x0007 offset: 0x370F
@scena.Code('func_07_370F')
def func_07_370F():
    @scena.Lambda('lambda_3715')
    def lambda_3715():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x000003E8)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_3715)

    OP_8E(0x00FE, -118000, 0, 64530, 2000, 0x00)
    OP_8E(0x00FE, -118910, 0, 64530, 2000, 0x00)
    ChrTurnDirection(0x00FE, 0x0008, 400)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
