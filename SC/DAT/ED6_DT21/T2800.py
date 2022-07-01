import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T2800_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T2800   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '蕾娜'),
    TXT(0x02, '布卢布兰的亡灵'),
    TXT(0x03, '王立学院·小道'),
    TXT(0x04, '街景林道方向'),
    TXT(0x05, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Ruan'
    header.mapModel       = 'T2800.x'
    header.mapIndex       = 1
    header.bgm            = 84
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 'ED6_DT21/SUB000._SN', 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x7FC
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
        ('ED6_DT26/CH20273._CH', 'ED6_DT26/CH20273P._CP'),
        ('ED6_DT07/CH01370._CH', 'ED6_DT07/CH01370P._CP'),
        ('ED6_DT26/CH20276._CH', 'ED6_DT26/CH20276P._CP'),
    ]

# id: 0x10002 offset: 0xC2
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = 31600,
            z                   = 0,
            y                   = 62470,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0003,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0185,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 84080,
            z                   = 0,
            y                   = 28010,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x00FF,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -3490,
            z                   = 0,
            y                   = 46180,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x00FF,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10003 offset: 0x142
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x142
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = 41180,
            y           = 0,
            z           = 74060,
            range       = 1000,
            dword_10    = 0x00000BB8,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000008,
        ),
        ScenaEventData(
            x           = 53030,
            y           = 0,
            z           = 67260,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000008,
        ),
        ScenaEventData(
            x           = 53150,
            y           = 0,
            z           = 59630,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000009,
        ),
        ScenaEventData(
            x           = 48380,
            y           = 0,
            z           = 45960,
            range       = 1000,
            dword_10    = 0x00000BB8,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000009,
        ),
        ScenaEventData(
            x           = 52870,
            y           = 0,
            z           = 32110,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000009,
        ),
        ScenaEventData(
            x           = 53030,
            y           = 0,
            z           = 24850,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x0000000A,
        ),
        ScenaEventData(
            x           = 47120,
            y           = 0,
            z           = 19010,
            range       = 1000,
            dword_10    = 0x00000BB8,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x0000000A,
        ),
        ScenaEventData(
            x           = 22030,
            y           = 0,
            z           = 25660,
            range       = 1000,
            dword_10    = 0x00000BB8,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x0000000B,
        ),
        ScenaEventData(
            x           = 22010,
            y           = 0,
            z           = 67170,
            range       = 1000,
            dword_10    = 0x00000BB8,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x0000000C,
        ),
    )

# id: 0x10005 offset: 0x262
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 65870,
            triggerZ            = 0,
            triggerY            = 27990,
            triggerRange        = 800,
            actorX              = 66000,
            actorZ              = 1000,
            actorY              = 28000,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0006,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 13480,
            triggerZ            = 1000,
            triggerY            = 46000,
            triggerRange        = 1000,
            actorX              = 13480,
            actorZ              = 1000,
            actorY              = 46000,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0007,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x2AA
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_2BD',
    )

    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 0x0004)

    def _loc_2BD(): pass

    label('loc_2BD')

    Return()

# id: 0x0001 offset: 0x2BE
@scena.Code('Init')
def Init():
    OP_16(0x02, 0x00000FA0, 0xFFFEA840, 0xFFFEBFB0, 0x0023004C)
    OP_72(0x0009, 0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0244, 3, 0x1223)),
            Expr.Return,
        ),
        'loc_2EA',
    )

    OP_64(0x00, 0x0001)
    OP_6F(0x000A, 60)

    Jump('loc_2F1')

    def _loc_2EA(): pass

    label('loc_2EA')

    OP_6F(0x000A, 0)

    def _loc_2F1(): pass

    label('loc_2F1')

    Return()

# id: 0x0002 offset: 0x2F2
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_307',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x000005DC)

    Jump('ReInit')

    def _loc_307(): pass

    label('loc_307')

    Return()

# id: 0x0003 offset: 0x308
@scena.Code('func_03_308')
def func_03_308():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_35B',
    )

    ChrTalk(
        0x00FE,
        (
            '在温度冷下来之前\n',
            '好像回不去宿舍呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '差不多我也该\n',
            '出手了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3D9')

    def _loc_35B(): pass

    label('loc_35B')

    OP_A2(0x0000)

    ChrTalk(
        0x00FE,
        (
            '呼……真糟糕。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '被芙拉瑟\n',
            '赶出房间了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然预料到会有排斥，\n',
            '没想到这么严重。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唔，差不多我也该\n',
            '出手了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3D9(): pass

    label('loc_3D9')

    TalkEnd(0x00FE)

    Return()

# id: 0x0004 offset: 0x3DD
@scena.Code('func_04_3DD')
def func_04_3DD():
    EventBegin(0x00)
    ClearMapFlags(0x00000010)
    OP_6D(69000, 7000, 17030, 0)
    OP_67(0, 8540, -10000, 0)
    OP_6B(3170, 0)
    OP_6C(286000, 0)
    OP_6E(439, 0)
    ClearChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x0009, 0x0001)
    SetChrPos(0x0009, 71000, 7000, 17030, 180)

    @scena.Lambda('lambda_0442')
    def lambda_0442():
        OP_9E(0x00FE, 0x00000000, 0x000000C8, 0x00000000, 0x000001F4)
        Yield()

        Jump('lambda_0442')

    DispatchAsync2(0x0009, 0x0003, lambda_0442)

    SetChrChipByIndex(0x0009, 0)
    SetChrSubChip(0x0009, 0)
    CreateThread(0x0009, 0x01, 0x01, 0x0005)
    OP_9F(0x0009, 0xFF, 0xFF, 0xFF, 0xB4, 0x00000000)
    OP_A0(0x0009, 0xB4, 0xB4, 0xB4, 0x00000000)
    FadeIn(2000, 0)

    @scena.Lambda('lambda_048E')
    def lambda_048E():
        OP_6B(2500, 8000)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_048E)

    OP_97(0x0009, 0x00010D88, 0x00004286, 0xFFFA81C0, 0x00000BB8, 0x0001)
    OP_97(0x0009, 0x00010D88, 0x00004286, 0xFFFA81C0, 0x00000BB8, 0x0001)
    OP_97(0x0009, 0x00010D88, 0x00004286, 0xFFFEA070, 0x000007D0, 0x0001)

    @scena.Lambda('lambda_04DD')
    def lambda_04DD():
        OP_6D(60990, 4000, 17030, 4000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_04DD)

    @scena.Lambda('lambda_04F5')
    def lambda_04F5():
        OP_6B(2600, 4000)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_04F5)

    @scena.Lambda('lambda_0505')
    def lambda_0505():
        OP_6E(307, 4000)

        ExitThread()

    DispatchAsync(0x0000, 0x0003, lambda_0505)

    Sleep(300)

    OP_8C(0x0009, 90, 1000)
    OP_8C(0x0009, 360, 1000)
    OP_8C(0x0009, 270, 1000)
    Sleep(300)

    Fade(500)

    @scena.Lambda('lambda_0539')
    def lambda_0539():
        OP_96(0x0009, 0x0000F60E, 0x00000FA0, 0x00004286, 0x000002BC, 0x000007D0)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_0539)

    OP_0D()
    TerminateThread(0x0009, 0x01)
    SetChrChipByIndex(0x0009, 2)
    SetChrSubChip(0x0009, 0)
    CreateThread(0x0009, 0x01, 0x01, 0x0005)
    OP_8C(0x0009, 270, 400)
    WaitForThreadExit(0x0000, 0x0003)
    Sleep(1000)

    OP_8C(0x0009, 90, 1000)
    OP_8C(0x0009, 360, 1000)
    OP_8C(0x0009, 270, 1000)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            '◆布卢布兰，优雅的ＡＰＬ表示。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(1000)

    TerminateThread(0x0009, 0x01)
    SetChrChipByIndex(0x0009, 0)
    SetChrSubChip(0x0009, 0)
    CreateThread(0x0009, 0x01, 0x01, 0x0005)

    @scena.Lambda('lambda_05E5')
    def lambda_05E5():
        OP_8E(0x00FE, 74000, 7000, 20300, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_05E5)

    Sleep(1000)

    FadeOut(2000, 0, -1)
    OP_0D()
    OP_A2(0x10F1)
    NewScene('ED6_DT21/T2511._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0005 offset: 0x617
@scena.Code('func_05_617')
def func_05_617():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_62C',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x000001F4)

    Jump('func_05_617')

    def _loc_62C(): pass

    label('loc_62C')

    Return()

# id: 0x0006 offset: 0x62D
@scena.Code('func_06_62D')
def func_06_62D():
    OP_22(0x0074, 0x00, 0x64)
    Sleep(300)

    OP_22(0x0074, 0x00, 0x64)
    Sleep(300)

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '后门上了锁。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)

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
            TXT(0x00, '【使用钥匙】\n'),
            TXT(0x01, '【不使用】\n'),
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
        (0x00000000, 'loc_6B0'),
        (-1, 'loc_77B'),
    )

    def _loc_6B0(): pass

    label('loc_6B0')

    EventBegin(0x00)
    Fade(1000)
    OP_6D(64870, 0, 27950, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(105000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0101, 64260, 0, 28070, 91)
    SetChrPos(0x00F7, 63120, 0, 29050, 85)
    SetChrPos(0x0105, 63880, 0, 27370, 105)
    SetChrPos(0x0104, 62150, 0, 28600, 100)
    SetChrPos(0x0127, 61540, 0, 27540, 74)
    OP_0D()
    OP_22(0x0073, 0x00, 0x64)
    Sleep(1000)

    OP_6F(0x000A, 0)
    OP_70(0x000A, 0x0000003C)
    OP_71(0x000A, 0x0002)
    OP_73(0x000A)
    OP_64(0x00, 0x0001)
    OP_A2(0x1223)
    Sleep(500)

    EventEnd(0x00)

    Jump('loc_77B')

    def _loc_77B(): pass

    label('loc_77B')

    FadeIn(300, 0)
    TalkEnd(0x00FF)

    Return()

# id: 0x0007 offset: 0x788
@scena.Code('func_07_788')
def func_07_788():
    OP_22(0x0074, 0x00, 0x64)
    Sleep(300)

    OP_22(0x0074, 0x00, 0x64)
    Sleep(300)

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '门上着锁。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x0008 offset: 0x7CE
@scena.Code('func_08_7CE')
def func_08_7CE():
    SetPlaceName(0x005F)

    Return()

# id: 0x0009 offset: 0x7D2
@scena.Code('func_09_7D2')
def func_09_7D2():
    SetPlaceName(0x005C)

    Return()

# id: 0x000A offset: 0x7D6
@scena.Code('func_0A_7D6')
def func_0A_7D6():
    SetPlaceName(0x005D)

    Return()

# id: 0x000B offset: 0x7DA
@scena.Code('func_0B_7DA')
def func_0B_7DA():
    SetPlaceName(0x006C)

    Return()

# id: 0x000C offset: 0x7DE
@scena.Code('func_0C_7DE')
def func_0C_7DE():
    SetPlaceName(0x006D)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
