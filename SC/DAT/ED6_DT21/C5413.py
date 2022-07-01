import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C5413_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C5413   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '怀斯曼教授'),
    TXT(0x02, '剑帝莱维'),
    TXT(0x03, '怪盗布卢布兰'),
    TXT(0x04, '幻惑之铃露茜奥拉'),
    TXT(0x05, '瘦狼瓦鲁特'),
    TXT(0x06, '歼灭天使玲'),
    TXT(0x07, '小丑肯帕雷拉'),
    TXT(0x08, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Other'
    header.mapModel       = 'C5413.x'
    header.mapIndex       = 1
    header.bgm            = 28
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x90F
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
        ('ED6_DT27/CH03550._CH', 'ED6_DT27/CH03550P._CP'),
        ('ED6_DT07/CH02040._CH', 'ED6_DT07/CH02040P._CP'),
        ('ED6_DT27/CH03530._CH', 'ED6_DT27/CH03530P._CP'),
        ('ED6_DT27/CH03520._CH', 'ED6_DT27/CH03520P._CP'),
        ('ED6_DT27/CH03500._CH', 'ED6_DT27/CH03500P._CP'),
        ('ED6_DT27/CH03510._CH', 'ED6_DT27/CH03510P._CP'),
        ('ED6_DT27/CH03600._CH', 'ED6_DT27/CH03600P._CP'),
        ('ED6_DT26/CH20280._CH', 'ED6_DT26/CH20280P._CP'),
    ]

# id: 0x10002 offset: 0xEA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10003 offset: 0x1CA
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x1CA
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x1CA
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x1CA
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 4, 0x10F4)),
            Expr.Return,
        ),
        'loc_1E1',
    )

    OP_A3(0x10F4)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x82),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Event(0, 0x0002)

    def _loc_1E1(): pass

    label('loc_1E1')

    Return()

# id: 0x0001 offset: 0x1E2
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_200',
    )

    ExecExpressionWithVar(
        0x3B,
        (
            (Expr.PushLong, 0x227),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x3C,
        (
            (Expr.PushLong, 0x10A),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_200(): pass

    label('loc_200')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C6, 0, 0x1E30)),
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_219',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_219(): pass

    label('loc_219')

    Return()

# id: 0x0002 offset: 0x21A
@scena.Code('ReInit')
def ReInit():
    EventBegin(0x00)
    SetChrFlags(0x0000, 0x0080)
    SetChrFlags(0x0001, 0x0080)
    SetChrFlags(0x0002, 0x0080)
    SetChrFlags(0x0003, 0x0080)
    OP_6D(780, 0, -76180, 0)
    OP_67(0, 14130, -10000, 0)
    OP_6B(4800, 0)
    OP_6C(48000, 0)
    OP_6E(834, 0)
    OP_22(0x01C3, 0x00, 0x64)
    OP_22(0x0131, 0x01, 0x46)
    SetChrPos(0x0008, 7490, 0, -52610, 90)
    SetChrPos(0x0009, 5870, 0, -52030, 90)
    SetChrPos(0x000D, 5130, 0, -53010, 90)
    SetChrPos(0x000A, 5550, 0, -54200, 90)
    SetChrPos(0x000C, 4720, 0, -55500, 90)
    SetChrPos(0x000B, 4860, 0, -51240, 90)
    SetChrPos(0x000E, 7500, 0, -54150, 90)
    ClearChrFlags(0x0008, 0x0080)
    ClearChrFlags(0x000E, 0x0080)
    ClearChrFlags(0x000A, 0x0080)
    ClearChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x000B, 0x0080)
    ClearChrFlags(0x000C, 0x0080)
    ClearChrFlags(0x000D, 0x0080)
    SetChrFlags(0x0000, 0x0080)
    SetChrFlags(0x0001, 0x0080)
    SetChrFlags(0x0002, 0x0080)
    SetChrFlags(0x0003, 0x0080)
    SetChrChipByIndex(0x000C, 7)
    SetChrSubChip(0x000C, 0)
    OP_C4(0x00, 0x00000002)
    OP_7E(0xBFBE, 0xE61A, 0xFDF8, 0x6E, 0x00000320)
    LoadEffect(0x01, 'map\\mp092_00.eff')
    PlayEffect(0x01, 0xFF, 0x00FF, 60000, 22000, 0, 180, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    @scena.Lambda('lambda_038F')
    def lambda_038F():
        OP_6D(30, 150, -38510, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_038F)

    FadeIn(1000, 0)
    OP_0D()
    WaitForThreadExit(0x0101, 0x0000)
    Fade(1000)
    PlayEffect(0x01, 0xFF, 0x00FF, 50000, 3000, 0, 180, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_6D(8000, 0, -52570, 0)
    OP_67(0, 5660, -10000, 0)
    OP_6B(2960, 0)
    OP_6C(65000, 0)
    OP_6E(322, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x000A,
        (
            '#0170341854V#233F#6P哦哦……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0210341855V#243F#6P这是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0200341856V#252F#6P哈哈……这是真的吗！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0220341857V#261F#6P呵呵……真不错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0190341858V#851F#6P哈哈！\n',
            '这个确实了不起！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0190341859V#854F难怪教授这么重视！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0150341860V#1154F#6P呵呵……\n',
            '你们喜欢就好。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150341861V#1151F『辉之环』长久以来\n',
            '被封印于异次元……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150341862V但是只要有了作为终端的『福音』，\n',
            '同样也能够影响到我们的次元。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150341863V问题是复制品的精确度\n',
            '能提升到什么样的程度。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0140341864V#125F#5P然后，在经过了多次实验后，\n',
            '真正的『福音』终于完成了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140341865V『环』透过它们已经\n',
            '拔出了连接自己的『桩』……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140341866V而现在从昏暗的深渊中苏醒了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140341867V#122F──这就是第三阶段的真相吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0150341868V#1155F#6P呵呵呵……没错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0726')
    def lambda_0726():
        OP_8C(0x00FE, 225, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0726)

    CreateThread(0x0008, 0x03, 0x00, 0x0003)
    FadeOut(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('怀斯曼教授')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#0150341869V多亏了诸位的奔波，\n',
            '第三阶段顺利完成！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150341870V接下来『福音计划』\n',
            '将进入最终阶段──',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_AD(0x002400B4, 0x0000, 0x0000, 0x00000064)
    WaitForThreadExit(0x0008, 0x0003)
    Sleep(4000)

    OP_56(0x02)
    OP_A2(0x1E30)

    ExecExpressionWithVar(
        0x31,
        (
            (Expr.PushLong, 0x129),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_C4(0x00, 0x00000010)
    OP_6D(-162160, 0, -33060, 0)
    FadeIn(0, 0)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    UnlockAchievement(0x14, 0x00, 0x00, 0x00)

    Menu(
        0,
        240,
        180,
        0,
        (
            TXT(0x00, '【保存进度】\n'),
            TXT(0x01, '【进入下一章】\n'),
        ),
    )

    MenuEnd(0x0000)
    OP_5F(0x0000)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_856',
    )

    ShowSaveMenu()

    def _loc_856(): pass

    label('loc_856')

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    FadeOut(0, 0, -1)
    OP_AE(0x000000C8)
    Sleep(2000)

    OP_20(0x000007D0)
    OP_21()
    OP_C4(0x01, 0x00000010)
    OP_A3(0x1E30)

    ExecExpressionWithVar(
        0x04,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_A2(0x10FD)
    NewScene('ED6_DT21/E0810._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0003 offset: 0x898
@scena.Code('func_03_898')
def func_03_898():
    OP_24(0x01C3, 0x5A)
    OP_24(0x0131, 0x41)
    Sleep(200)

    OP_24(0x01C3, 0x50)
    OP_24(0x0131, 0x3C)
    Sleep(200)

    OP_24(0x01C3, 0x46)
    OP_24(0x0131, 0x37)
    Sleep(200)

    OP_24(0x01C3, 0x3C)
    OP_24(0x0131, 0x32)
    Sleep(200)

    OP_24(0x01C3, 0x32)
    OP_24(0x0131, 0x2D)
    Sleep(200)

    OP_24(0x01C3, 0x28)
    OP_24(0x0131, 0x28)
    Sleep(200)

    OP_24(0x01C3, 0x1E)
    OP_24(0x0131, 0x1E)
    Sleep(200)

    OP_24(0x01C3, 0x14)
    OP_24(0x0131, 0x14)
    Sleep(200)

    OP_23(0x01C3)
    OP_23(0x0131)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
