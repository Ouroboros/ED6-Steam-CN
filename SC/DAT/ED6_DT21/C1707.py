import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C1707_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C1707   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '歼灭天使玲'),
    TXT(0x02, '福音'),
    TXT(0x03, '帕蒂尔·玛蒂尔'),
    TXT(0x04, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Bose'
    header.mapModel       = 'C1707.x'
    header.mapIndex       = 1
    header.bgm            = 10
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x1209
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
        ('ED6_DT27/CH04510._CH', 'ED6_DT27/CH04510P._CP'),
        ('ED6_DT06/CH20020._CH', 'ED6_DT06/CH20020P._CP'),
        ('ED6_DT27/CH04000._CH', 'ED6_DT27/CH04000P._CP'),
        ('ED6_DT27/CH04010._CH', 'ED6_DT27/CH04010P._CP'),
    ]

# id: 0x10002 offset: 0xCA
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
            dword_10            = 458753,
            chipIndex           = 1,
            npcIndex            = 0x01E6,
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
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x01C5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10003 offset: 0x12A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x12A
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x12A
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x12A
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_141',
    )

    OP_A3(0x10F0)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x53),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Event(0, 0x0002)

    def _loc_141(): pass

    label('loc_141')

    Return()

# id: 0x0001 offset: 0x142
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_156',
    )

    OP_B1('C1707_y')

    Jump('loc_15F')

    def _loc_156(): pass

    label('loc_156')

    OP_B1('C1707_n')

    def _loc_15F(): pass

    label('loc_15F')

    Return()

# id: 0x0002 offset: 0x160
@scena.Code('ReInit')
def ReInit():
    EventBegin(0x00)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_177',
    )

    Call(0, 0x0003)
    Call(0, 0x0004)

    def _loc_177(): pass

    label('loc_177')

    OP_82(0x80, 0x00)
    OP_82(0x82, 0x00)
    OP_72(0x0009, 0x0004)
    OP_72(0x0008, 0x0004)
    OP_71(0x0007, 0x0004)
    OP_71(0x0002, 0x0004)
    OP_71(0x0003, 0x0004)
    OP_71(0x0004, 0x0004)
    OP_71(0x0005, 0x0004)
    OP_71(0x0006, 0x0004)
    OP_79(0x00, 0x0002)
    OP_79(0x01, 0x0002)
    OP_79(0x02, 0x0002)
    OP_79(0x03, 0x0002)
    OP_79(0x04, 0x0002)
    OP_7B()
    LoadEffect(0x01, 'map\\\\mp021_00.eff')
    LoadEffect(0x02, 'map\\\\mp064_01.eff')
    LoadEffect(0x03, 'map\\\\mp065_01.eff')
    LoadEffect(0x04, 'map\\\\mp064_00.eff')
    LoadEffect(0x05, 'map\\\\mp065_00.eff')
    OP_72(0x0000, 0x0004)
    OP_A1(0x000A, 0x0000)
    SetChrPos(0x000A, 10580, 500, 9330, 225)
    OP_71(0x0000, 0x0020)
    OP_B0(0x0000, 0x14)
    OP_6F(0x0000, 381)
    OP_70(0x0000, 0x000001A4)
    ClearChrFlags(0x000A, 0x0080)
    SetChrFlags(0x000A, 0x0001)

    ExecExpressionWithValue(
        0x000A,
        0x28,
        (
            (Expr.PushLong, 0x2),
            (Expr.PushLong, 0x1),
            Expr.Or,
            (Expr.PushLong, 0x8),
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000A,
        0x07,
        (
            (Expr.PushLong, 0x1770),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000A,
        0x34,
        (
            (Expr.PushLong, 0xEA60),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearMapFlags(0x00000040)
    SetChrPos(0x0101, 1200, 0, 1200, 45)
    SetChrPos(0x0102, 870, 0, 2560, 45)
    SetChrPos(0x00F8, -50, 0, 110, 45)
    SetChrPos(0x00F9, -450, 0, 1740, 45)
    SetChrSubChip(0x0101, 0)
    SetChrChipByIndex(0x0101, 65535)
    SetChrSubChip(0x0102, 0)
    SetChrChipByIndex(0x0102, 65535)
    SetChrSubChip(0x00F8, 0)
    SetChrChipByIndex(0x00F8, 65535)
    SetChrSubChip(0x00F9, 0)
    SetChrChipByIndex(0x00F9, 65535)
    SetChrPos(0x0008, 1220, 950, 12420, 0)
    ClearChrFlags(0x0008, 0x0080)
    SetChrFlags(0x0008, 0x0010)
    SetChrChipByIndex(0x0008, 0)
    SetChrSubChip(0x0008, 0)
    ClearChrFlags(0x0008, 0x0001)
    OP_CF(0x0008, 0x00, 'Frame85__ren')

    ExecExpressionWithValue(
        0x0008,
        0x24,
        (
            (Expr.PushLong, 0xA5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_6D(34920, 250, 12030, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3960, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_22(0x01C3, 0x00, 0x64)

    @scena.Lambda('lambda_0386')
    def lambda_0386():
        OP_6D(6260, 250, 8340, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_0386)

    @scena.Lambda('lambda_039E')
    def lambda_039E():
        OP_67(0, 5950, -10000, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_039E)

    @scena.Lambda('lambda_03B6')
    def lambda_03B6():
        OP_6B(4940, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_03B6)

    FadeIn(1000, 0)
    OP_0D()
    Sleep(1000)

    WaitForThreadExit(0x0101, 0x0000)
    Fade(500)
    OP_71(0x0008, 0x0004)
    OP_6D(7230, 250, 9770, 0)
    OP_67(0, 3510, -10000, 0)
    OP_6B(5260, 0)
    OP_6C(32000, 0)
    OP_6E(243, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010341718V#1026F#5P恢、恢复了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020341719V#1042F#5P『塔』已经解放了吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0220341720V#1302F#6P……真无趣。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220341721V时间再多一点的话，\n',
            '就能把你们全部杀光了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    OP_22(0x0113, 0x01, 0x46)
    OP_22(0x0114, 0x00, 0x64)
    PlayEffect(0x01, 0x00, 0x000A, 0, -500, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_22(0x00CC, 0x00, 0x64)
    PlayEffect(0x04, 0x01, 0x000A, 4950, 2800, 0, 0, 0, 20, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x04, 0x02, 0x000A, -4950, 2800, 0, 0, 0, 340, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(500)

    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(100)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5EB',
    )

    OP_62(0x00F8, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    Jump('loc_629')

    def _loc_5EB(): pass

    label('loc_5EB')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_612',
    )

    OP_62(0x00F8, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    Jump('loc_629')

    def _loc_612(): pass

    label('loc_612')

    OP_62(0x00F8, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    def _loc_629(): pass

    label('loc_629')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_650',
    )

    OP_62(0x00F9, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    Jump('loc_68E')

    def _loc_650(): pass

    label('loc_650')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_677',
    )

    OP_62(0x00F9, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    Jump('loc_68E')

    def _loc_677(): pass

    label('loc_677')

    OP_62(0x00F9, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    def _loc_68E(): pass

    label('loc_68E')

    Sleep(1000)

    @scena.Lambda('lambda_0699')
    def lambda_0699():
        OP_8C(0x00FE, 45, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0699)

    @scena.Lambda('lambda_06A7')
    def lambda_06A7():
        OP_8C(0x00FE, 45, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_06A7)

    Sleep(100)

    @scena.Lambda('lambda_06BA')
    def lambda_06BA():
        OP_8C(0x00FE, 45, 400)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_06BA)

    OP_8C(0x00F9, 45, 400)

    ChrTalk(
        0x0101,
        (
            '#0010341722V#1005F#5P慢、慢着！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0220341723V#1306F#6P哈哈哈……\n',
            '玲要回『古罗力亚斯』了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220341724V教授说过，『β』一旦完成\n',
            '就让玲回去的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010341725V#1020F#5P教、教授！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020341726V#1044F#5P『β』已经完成了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020341727V#1046F恢复『塔』的原样\n',
            '也是计划的一部分吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0220341728V#263F#6P谁知道？\n',
            '玲也不怎么清楚。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220341729V#1305F不过，听说笼罩这里的结界\n',
            '是『环』的“手”。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010341730V#1026F#5P『辉之环』的……手！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0220341731V#261F#6P嘻嘻……\n',
            '会是什么意思呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearMapFlags(0x00000010)

    @scena.Lambda('lambda_08DE')
    def lambda_08DE():
        OP_6D(11800, 4800, 10810, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_08DE)

    @scena.Lambda('lambda_08F6')
    def lambda_08F6():
        OP_67(0, 3560, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_08F6)

    @scena.Lambda('lambda_090E')
    def lambda_090E():
        OP_6B(3450, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_090E)

    @scena.Lambda('lambda_091E')
    def lambda_091E():
        OP_6C(41000, 3000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_091E)

    @scena.Lambda('lambda_092E')
    def lambda_092E():
        OP_6E(325, 3000)

        ExitThread()

    DispatchAsync(0x0102, 0x0003, lambda_092E)

    PlayEffect(0x02, 0x01, 0x000A, 5000, 2500, 0, 0, 0, 20, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x02, 0x02, 0x000A, -4900, 2500, 0, 0, 0, 340, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    @scena.Lambda('lambda_09A8')
    def lambda_09A8():
        OP_8F(0x00FE, 10580, 2500, 9330, 500, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_09A8)

    Sleep(300)

    @scena.Lambda('lambda_09C8')
    def lambda_09C8():
        OP_8F(0x00FE, 10580, 2500, 9330, 750, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_09C8)

    Sleep(300)

    @scena.Lambda('lambda_09E8')
    def lambda_09E8():
        OP_8F(0x00FE, 10580, 2500, 9330, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_09E8)

    OP_24(0x0113, 0x50)
    Sleep(100)

    OP_72(0x0000, 0x0020)
    OP_D8(0x00, 0x01F4)
    OP_6F(0x0000, 241)
    OP_70(0x0000, 0x00000104)
    OP_82(0x00, 0x02)
    Sleep(50)

    PlayEffect(0x02, 0x01, 0x000A, 4600, 2600, 0, 0, 0, 18, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x02, 0x02, 0x000A, -4600, 2600, 0, 0, 0, 342, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(250)

    @scena.Lambda('lambda_0A9A')
    def lambda_0A9A():
        OP_8F(0x00FE, 10580, 2500, 9330, 750, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_0A9A)

    OP_24(0x0113, 0x5A)
    Sleep(100)

    OP_24(0x0113, 0x64)
    WaitForThreadExit(0x000A, 0x0001)
    WaitForThreadExit(0x0101, 0x0001)
    SetChrSubChip(0x0008, 0)
    WaitForThreadExit(0x0101, 0x0001)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0220341732V#263F#5P哈哈哈，那么再见了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220341733V#1304F下次见面时──\n',
            '我会把你们全部杀掉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0B40')
    def lambda_0B40():
        OP_8C(0x00FE, 80, 10)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_0B40)

    Sleep(200)

    @scena.Lambda('lambda_0B53')
    def lambda_0B53():
        OP_8C(0x00FE, 80, 15)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_0B53)

    Sleep(200)

    @scena.Lambda('lambda_0B66')
    def lambda_0B66():
        OP_8C(0x00FE, 80, 20)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_0B66)

    Sleep(500)

    @scena.Lambda('lambda_0B79')
    def lambda_0B79():
        OP_8C(0x00FE, 80, 30)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_0B79)

    Sleep(100)

    @scena.Lambda('lambda_0B8C')
    def lambda_0B8C():
        OP_8C(0x00FE, 80, 40)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_0B8C)

    Sleep(2500)

    Fade(500)
    OP_6D(16090, 5040, 13150, 0)
    OP_67(0, 3440, -10000, 0)
    OP_6B(3690, 0)
    OP_6C(39000, 0)
    OP_6E(325, 0)
    ClearChrFlags(0x000A, 0x0001)

    @scena.Lambda('lambda_0BE6')
    def lambda_0BE6():
        OP_8C(0x00FE, 80, 20)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_0BE6)

    Sleep(500)

    @scena.Lambda('lambda_0BF9')
    def lambda_0BF9():
        OP_8C(0x00FE, 80, 15)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_0BF9)

    Sleep(500)

    @scena.Lambda('lambda_0C0C')
    def lambda_0C0C():
        OP_8C(0x00FE, 80, 10)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_0C0C)

    WaitForThreadExit(0x000A, 0x0002)

    @scena.Lambda('lambda_0C1F')
    def lambda_0C1F():
        OP_6B(3900, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0C1F)

    OP_72(0x0000, 0x0020)
    OP_D8(0x00, 0x01F4)
    OP_6F(0x0000, 261)
    OP_70(0x0000, 0x00000118)
    OP_22(0x0116, 0x00, 0x64)
    OP_73(0x0000)
    Sleep(500)

    PlayEffect(0x03, 0x00, 0x000A, 500, -3300, -3600, 0, 80, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x03, 0x03, 0x000A, -500, -3300, -3600, 0, 80, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x04, 0x04, 0x000A, 1000, -2600, -3000, 0, 70, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x04, 0x05, 0x000A, 400, -2600, -3000, 0, 70, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x04, 0x06, 0x000A, -1000, -2600, -3000, 0, 70, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x04, 0x07, 0x000A, -400, -2600, -3000, 0, 70, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_22(0x0114, 0x00, 0x64)
    Sleep(2000)

    PlayEffect(0x02, 0x00, 0x000A, 500, -3300, -3600, 0, 80, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x02, 0x03, 0x000A, -500, -3300, -3600, 0, 80, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x03, 0x04, 0x000A, 1000, -2600, -3000, 0, 70, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x03, 0x05, 0x000A, 400, -2600, -3000, 0, 70, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x03, 0x06, 0x000A, -1000, -2600, -3000, 0, 70, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x03, 0x07, 0x000A, -400, -2600, -3000, 0, 70, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_71(0x0000, 0x0020)
    OP_6F(0x0000, 281)
    OP_70(0x0000, 0x0000012C)
    OP_82(0x01, 0x02)
    OP_82(0x02, 0x02)
    Sleep(500)

    @scena.Lambda('lambda_0EF7')
    def lambda_0EF7():
        OP_6D(16040, 8000, 13170, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_0EF7)

    @scena.Lambda('lambda_0F0F')
    def lambda_0F0F():
        OP_67(0, 690, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0F0F)

    @scena.Lambda('lambda_0F27')
    def lambda_0F27():
        OP_6C(75000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0F27)

    @scena.Lambda('lambda_0F37')
    def lambda_0F37():
        OP_6E(548, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0F37)

    @scena.Lambda('lambda_0F47')
    def lambda_0F47():
        OP_8F(0x00FE, 153960, 25000, 20580, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_0F47)

    Sleep(100)

    @scena.Lambda('lambda_0F67')
    def lambda_0F67():
        OP_8F(0x00FE, 153960, 25000, 20580, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_0F67)

    Sleep(100)

    @scena.Lambda('lambda_0F87')
    def lambda_0F87():
        OP_8F(0x00FE, 1503960, 25000, 20580, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_0F87)

    Sleep(100)

    @scena.Lambda('lambda_0FA7')
    def lambda_0FA7():
        OP_8F(0x00FE, 153960, 25000, 20580, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_0FA7)

    Sleep(100)

    @scena.Lambda('lambda_0FC7')
    def lambda_0FC7():
        OP_8F(0x00FE, 153960, 25000, 20580, 13000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_0FC7)

    Sleep(100)

    @scena.Lambda('lambda_0FE7')
    def lambda_0FE7():
        OP_8F(0x00FE, 153960, 30000, 20580, 18000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_0FE7)

    Sleep(100)

    @scena.Lambda('lambda_1007')
    def lambda_1007():
        OP_8F(0x00FE, 153960, 30000, 20580, 23000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_1007)

    Sleep(100)

    @scena.Lambda('lambda_1027')
    def lambda_1027():
        OP_8F(0x00FE, 153960, 30000, 20580, 28000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_1027)

    Sleep(100)

    @scena.Lambda('lambda_1047')
    def lambda_1047():
        OP_8F(0x00FE, 153960, 40000, 20580, 33000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_1047)

    Sleep(100)

    @scena.Lambda('lambda_1067')
    def lambda_1067():
        OP_8F(0x00FE, 153960, 40000, 20580, 38000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_1067)

    Sleep(100)

    @scena.Lambda('lambda_1087')
    def lambda_1087():
        OP_8F(0x00FE, 153960, 50000, 20580, 43000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_1087)

    Sleep(100)

    @scena.Lambda('lambda_10A7')
    def lambda_10A7():
        OP_8F(0x00FE, 153960, 50000, 20580, 48000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_10A7)

    WaitForThreadExit(0x000A, 0x0001)
    WaitForThreadExit(0x0101, 0x0001)
    FadeOut(1000, 0, -1)
    OP_0D()
    OP_A2(0x1E24)
    SetMapFlags(0x00100000)
    OP_A2(0x10FF)
    OP_A2(0x10F5)
    NewScene('ED6_DT21/E0810._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0003 offset: 0x10E9
@scena.Code('func_03_10E9')
def func_03_10E9():
    FadeOut(0, 0, -1)
    OP_A3(0x1200)
    OP_A3(0x1201)
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x05, 0xFF)

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
        100,
        0,
        (
            TXT(0x00, '【◇选择雪拉扎德为队友】\n'),
            TXT(0x01, '【◇选择阿加特为队友】\n'),
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
    OP_56(0x00)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_1163'),
        (0x00000001, 'loc_1169'),
        (-1, 'loc_116F'),
    )

    def _loc_1163(): pass

    label('loc_1163')

    OP_A2(0x1200)

    Jump('loc_116F')

    def _loc_1169(): pass

    label('loc_1169')

    OP_A2(0x1201)

    Jump('loc_116F')

    def _loc_116F(): pass

    label('loc_116F')

    Return()

# id: 0x0004 offset: 0x1170
@scena.Code('func_04_1170')
def func_04_1170():
    FadeOut(0, 0, -1)
    OP_6D(-66940, 250, 36210, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(3700, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    Sleep(200)

    FadeIn(0, 0)
    OP_0D()

    OP_C9(
        0x00,
        (
            0x0000,
            0x0001,
            0x00FF,
            0x00FF,
        ),
        (
            0x0005,
            0x0002,
            0x0006,
            0x0004,
            0x0007,
            0x0008,
            0xFFFF,
        ),
    )

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(100)

    FadeOut(0, 0, -1)
    OP_69(0x0000, 0x00000000)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
