import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import E0110_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('E0110   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '吉尔'),
    TXT(0x02, '乔丝特'),
    TXT(0x03, '空贼雷古'),
    TXT(0x04, '空贼蒂诺'),
    TXT(0x05, '空贼莱尔'),
    TXT(0x06, '空贼洛西'),
    TXT(0x07, '空贼罗尔'),
    TXT(0x08, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'event'
    header.mapModel       = 'E0110.x'
    header.mapIndex       = 1
    header.bgm            = 87
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0xB00
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
        ('ED6_DT07/CH02120._CH', 'ED6_DT07/CH02120P._CP'),
        ('ED6_DT07/CH02130._CH', 'ED6_DT07/CH02130P._CP'),
        ('ED6_DT07/CH01380._CH', 'ED6_DT07/CH01380P._CP'),
    ]

# id: 0x10002 offset: 0xC2
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = -24246,
            z                   = -1000,
            y                   = 4880,
            direction           = 270,
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
            x                   = -18320,
            z                   = 3000,
            y                   = 4790,
            direction           = 270,
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
            x                   = -21660,
            z                   = 650,
            y                   = 5320,
            direction           = 290,
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
            x                   = 45400,
            z                   = 0,
            y                   = 6950,
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
            x                   = 51600,
            z                   = 0,
            y                   = 3170,
            direction           = 135,
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
            x                   = 47800,
            z                   = 0,
            y                   = 6490,
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
            x                   = 52600,
            z                   = 0,
            y                   = 3890,
            direction           = 135,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10003 offset: 0x1A2
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x1A2
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x1A2
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x1A2
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 2, 0x3FA)),
            Expr.Return,
        ),
        'loc_1D3',
    )

    ClearChrFlags(0x0008, 0x0080)
    ClearChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x000A, 0x0080)
    ClearChrFlags(0x000B, 0x0080)
    ClearChrFlags(0x000C, 0x0080)
    ClearChrFlags(0x000D, 0x0080)
    ClearChrFlags(0x000E, 0x0080)
    ClearScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    Event(0, 0x0003)

    def _loc_1D3(): pass

    label('loc_1D3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 3, 0x3FB)),
            Expr.Return,
        ),
        'loc_204',
    )

    ClearChrFlags(0x0008, 0x0080)
    ClearChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x000A, 0x0080)
    ClearChrFlags(0x000B, 0x0080)
    ClearChrFlags(0x000C, 0x0080)
    ClearChrFlags(0x000D, 0x0080)
    ClearChrFlags(0x000E, 0x0080)
    ClearScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))
    Event(0, 0x0005)

    def _loc_204(): pass

    label('loc_204')

    Return()

# id: 0x0001 offset: 0x205
@scena.Code('Init')
def Init():
    PlaySE(122, 0x00, 0x64)

    Return()

# id: 0x0002 offset: 0x20B
@scena.Code('ReInit')
def ReInit():
    ExecExpressionWithReg(
        0x0000,
        (
            Expr.Rand,
            (Expr.PushLong, 0xE),
            Expr.Mod,
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_230',
    )

    OP_99(0x00FE, 0x00, 0x07, 1650)

    Jump('loc_372')

    def _loc_230(): pass

    label('loc_230')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_249',
    )

    OP_99(0x00FE, 0x01, 0x07, 1600)

    Jump('loc_372')

    def _loc_249(): pass

    label('loc_249')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_262',
    )

    OP_99(0x00FE, 0x02, 0x07, 1550)

    Jump('loc_372')

    def _loc_262(): pass

    label('loc_262')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_27B',
    )

    OP_99(0x00FE, 0x03, 0x07, 1500)

    Jump('loc_372')

    def _loc_27B(): pass

    label('loc_27B')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_294',
    )

    OP_99(0x00FE, 0x04, 0x07, 1450)

    Jump('loc_372')

    def _loc_294(): pass

    label('loc_294')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2AD',
    )

    OP_99(0x00FE, 0x05, 0x07, 1400)

    Jump('loc_372')

    def _loc_2AD(): pass

    label('loc_2AD')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2C6',
    )

    OP_99(0x00FE, 0x06, 0x07, 1350)

    Jump('loc_372')

    def _loc_2C6(): pass

    label('loc_2C6')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2DF',
    )

    OP_99(0x00FE, 0x00, 0x07, 1655)

    Jump('loc_372')

    def _loc_2DF(): pass

    label('loc_2DF')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2F8',
    )

    OP_99(0x00FE, 0x01, 0x07, 1605)

    Jump('loc_372')

    def _loc_2F8(): pass

    label('loc_2F8')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_311',
    )

    OP_99(0x00FE, 0x02, 0x07, 1555)

    Jump('loc_372')

    def _loc_311(): pass

    label('loc_311')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_32A',
    )

    OP_99(0x00FE, 0x03, 0x07, 1505)

    Jump('loc_372')

    def _loc_32A(): pass

    label('loc_32A')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xB),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_343',
    )

    OP_99(0x00FE, 0x04, 0x07, 1455)

    Jump('loc_372')

    def _loc_343(): pass

    label('loc_343')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xC),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_35C',
    )

    OP_99(0x00FE, 0x05, 0x07, 1405)

    Jump('loc_372')

    def _loc_35C(): pass

    label('loc_35C')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xD),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_372',
    )

    OP_99(0x00FE, 0x06, 0x07, 1355)

    def _loc_372(): pass

    label('loc_372')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_387',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('loc_372')

    def _loc_387(): pass

    label('loc_387')

    Return()

# id: 0x0003 offset: 0x388
@scena.Code('func_03_388')
def func_03_388():
    ClearMapFlags(0x00000001)
    EventBegin(0x00)
    SetChrPos(0x0101, 51687, 0, 77948, 225)
    SetChrPos(0x0102, 51687, 0, 77948, 225)
    SetChrPos(0x0103, 51687, 0, 77948, 225)
    SetChrPos(0x0104, 51687, 0, 77948, 225)
    CameraMove(-28590, -250, 8210, 0)
    OP_67(0, 6000, -10000, 0)
    CameraSetDistance(3000, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    OP_75(0x04, 0x00000005, 0x05)
    OP_74(0x0004, 0x00000005, 0x0000)
    FadeIn(2000, 0)
    CameraMove(-23750, -500, 7540, 3000)

    ChrTalk(
        0x0009,
        (
            '#0090031342V#210F气温２１度，湿度１５％。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090031343V南南西，风速１２亚矩。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090031344V周围没有导力反应。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0290031345V#200F好像也没有军队巡逻……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0290031346V开动导力引擎。\n',
            '开始向船体各部分传送导力。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1040031347V收到。\n',
            '开动导力引擎。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_74(0x0004, 0x00000005, 0x0000)
    Sleep(100)

    OP_74(0x0004, 0x00000005, 0x0001)
    Sleep(100)

    OP_74(0x0004, 0x00000005, 0x0002)
    Sleep(100)

    OP_74(0x0004, 0x00000005, 0x0003)
    Sleep(100)

    OP_74(0x0004, 0x00000005, 0x0004)
    Sleep(100)

    OP_74(0x0004, 0x00000005, 0x0005)
    Sleep(100)

    OP_74(0x0004, 0x00000005, 0x0006)
    Sleep(100)

    OP_74(0x0004, 0x00000005, 0x0007)
    Sleep(100)

    CreateThread(0x000A, 0x03, 0x00, 0x0004)
    Sleep(500)

    ChrTalk(
        0x000A,
        (
            '#1040031348V开始向各部分传送导力。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(1000)
    CameraMove(48020, 0, 5490, 0)
    OP_0D()

    ChrTalk(
        0x000C,
        (
            '#0990031349V#3P导力浮板开始运作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#1270031350V导力驱动开始运作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#1050031351V水平尾翼也ＯＫ了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(1000)
    CameraMove(-22333, 650, 4849, 0)
    OP_0D()

    ChrTalk(
        0x0008,
        (
            '#0290031352V#200F好了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0290031353V#201F卡普亚空贼团所属的『山猫号』\n',
            '——起航！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1040031354V收到。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))
    SetMapFlags(0x02000000)
    NewScene('ED6_DT01/R1403._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0004 offset: 0x6C5
@scena.Code('func_04_6C5')
def func_04_6C5():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_741',
    )

    OP_74(0x0004, 0x00000005, 0x0008)
    Sleep(100)

    OP_74(0x0004, 0x00000005, 0x0009)
    Sleep(100)

    OP_74(0x0004, 0x00000005, 0x000A)
    Sleep(100)

    OP_74(0x0004, 0x00000005, 0x000B)
    Sleep(100)

    OP_74(0x0004, 0x00000005, 0x000C)
    Sleep(100)

    OP_74(0x0004, 0x00000005, 0x000D)
    Sleep(100)

    OP_74(0x0004, 0x00000005, 0x000E)
    Sleep(100)

    OP_74(0x0004, 0x00000005, 0x000F)
    Sleep(100)

    Jump('func_04_6C5')

    def _loc_741(): pass

    label('loc_741')

    Return()

# id: 0x0005 offset: 0x742
@scena.Code('func_05_742')
def func_05_742():
    ClearMapFlags(0x00000001)
    EventBegin(0x00)
    OP_71(0x0002, 0x0004)
    OP_72(0x0001, 0x0004)
    OP_72(0x0003, 0x0004)
    OP_72(0x0005, 0x0004)
    OP_72(0x0006, 0x0004)
    OP_72(0x0007, 0x0004)
    OP_72(0x0008, 0x0004)
    OP_72(0x0009, 0x0004)
    OP_7A(0x09, 0x0002)
    OP_7B()
    CameraMove(-23750, -500, 7540, 0)
    SetChrPos(0x0101, 51687, 0, 77948, 100)
    SetChrPos(0x0102, 51187, 0, 77448, 100)
    SetChrPos(0x0103, 51187, 0, 77448, 100)
    SetChrPos(0x0104, 51187, 0, 77448, 100)
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#0290031355V#200F驱动率固定在４０％。\n',
            '就这样维持航行速度。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0290031356V不过，\n',
            '要随时准备将其切换成战斗速度。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1040031357V收到。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0090031358V#211F哈哈，\n',
            '天亮前应该就能到了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0290031359V#200F是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0290031360V虽然很想早点休息，\n',
            '不过必须先向多伦大哥报告一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CreateThread(0x000B, 0x01, 0x00, 0x0002)
    CreateThread(0x000D, 0x01, 0x00, 0x0002)
    Sleep(300)

    Fade(1000)
    CameraMove(48020, 0, 5490, 0)
    Sleep(1500)

    PlaySE(130, 0x00, 0x64)
    Sleep(500)

    OP_62(0x000E, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)
    Sleep(1500)

    SetChrDirection(0x000E, 0, 400)
    Sleep(200)

    ChrTalk(
        0x000E,
        (
            '#1270031361V……咦…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#1270031362V好像有什么声音。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000C, 0x000E, 400)
    Sleep(200)

    ChrTalk(
        0x000C,
        (
            '#0990031363V#3P唔？\n',
            '我什么也没听见啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#1270031364V好奇怪。\n',
            '应该是从船舱的方向……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrWalkTo(0x000E, 51875, 0, 6916, 3000, 0x00)
    ChrWalkTo(0x000E, 49264, -2000, 6916, 3000, 0x00)
    Fade(1000)
    CameraMove(47960, 0, 77660, 0)
    SetChrPos(0x000E, 50750, 1500, 77980, 0)
    ChrWalkTo(0x000E, 48128, 0, 77568, 3000, 0x00)
    SetChrDirection(0x000E, 180, 400)

    ChrTalk(
        0x000E,
        (
            '#1270031365V啊……\n',
            '也许是老鼠吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#1270031366V有空再打扫一下好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x000E, 90, 400)
    ChrWalkTo(0x000E, 50820, 1500, 77900, 3000, 0x00)

    @scena.Lambda('lambda_0A90')
    def lambda_0A90():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 500)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_0A90)

    @scena.Lambda('lambda_0AA2')
    def lambda_0AA2():
        ChrWalkTo(0x00FE, 53150, 3000, 77790, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0002, lambda_0AA2)

    Sleep(1000)

    @scena.Lambda('lambda_0AC2')
    def lambda_0AC2():
        CameraSetDistance(2400, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0AC2)

    CameraMove(52782, 0, 77100, 5000)
    SetChrFlags(0x000E, 0x0080)
    OP_20(0x000007D0)
    SetScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    NewScene('ED6_DT01/C1401._SN', 100, 0, 0)
    IdleLoop()

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
