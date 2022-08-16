import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C5613_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C5613   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Other'
    header.mapModel       = 'C5613.x'
    header.mapIndex       = 1
    header.bgm            = 61
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x64
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

# id: 0x10000 offset: 0xA8
@scena.ChipData('ChipData')
def ChipData():
    return [
        # (ch, cp)
        ('ED6_DT29/CH12570._CH', 'ED6_DT29/CH12570P._CP'),
        ('ED6_DT29/CH12571._CH', 'ED6_DT29/CH12571P._CP'),
        ('ED6_DT29/CH12320._CH', 'ED6_DT29/CH12320P._CP'),
        ('ED6_DT29/CH12321._CH', 'ED6_DT29/CH12321P._CP'),
        ('ED6_DT29/CH12330._CH', 'ED6_DT29/CH12330P._CP'),
        ('ED6_DT29/CH12331._CH', 'ED6_DT29/CH12331P._CP'),
        ('ED6_DT29/CH12350._CH', 'ED6_DT29/CH12350P._CP'),
        ('ED6_DT29/CH12351._CH', 'ED6_DT29/CH12351P._CP'),
        ('ED6_DT29/CH12000._CH', 'ED6_DT29/CH12000P._CP'),
        ('ED6_DT29/CH12201._CH', 'ED6_DT29/CH12201P._CP'),
        ('ED6_DT26/CH20375._CH', 'ED6_DT26/CH20375P._CP'),
        ('ED6_DT27/CH03005._CH', 'ED6_DT27/CH03005P._CP'),
        ('ED6_DT27/CH04560._CH', 'ED6_DT27/CH04560P._CP'),
        ('ED6_DT27/CH04561._CH', 'ED6_DT27/CH04561P._CP'),
        ('ED6_DT07/CH00112._CH', 'ED6_DT07/CH00112P._CP'),
        ('ED6_DT26/CH20377._CH', 'ED6_DT26/CH20377P._CP'),
        ('ED6_DT27/CH04000._CH', 'ED6_DT27/CH04000P._CP'),
        ('ED6_DT27/CH04004._CH', 'ED6_DT27/CH04004P._CP'),
        ('ED6_DT07/CH00124._CH', 'ED6_DT07/CH00124P._CP'),
        ('ED6_DT07/CH00154._CH', 'ED6_DT07/CH00154P._CP'),
        ('ED6_DT07/CH00134._CH', 'ED6_DT07/CH00134P._CP'),
        ('ED6_DT07/CH00144._CH', 'ED6_DT07/CH00144P._CP'),
        ('ED6_DT07/CH00164._CH', 'ED6_DT07/CH00164P._CP'),
        ('ED6_DT07/CH00174._CH', 'ED6_DT07/CH00174P._CP'),
        ('ED6_DT27/CH04084._CH', 'ED6_DT27/CH04084P._CP'),
        ('ED6_DT27/CH03510._CH', 'ED6_DT27/CH03510P._CP'),
        ('ED6_DT07/CH02040._CH', 'ED6_DT07/CH02040P._CP'),
        ('ED6_DT26/CH20378._CH', 'ED6_DT26/CH20378P._CP'),
        ('ED6_DT27/CH03550._CH', 'ED6_DT27/CH03550P._CP'),
        ('ED6_DT26/CH20212._CH', 'ED6_DT26/CH20212P._CP'),
        ('ED6_DT26/CH20215._CH', 'ED6_DT26/CH20215P._CP'),
        ('ED6_DT26/CH20213._CH', 'ED6_DT26/CH20213P._CP'),
        ('ED6_DT26/CH20214._CH', 'ED6_DT26/CH20214P._CP'),
        ('ED6_DT26/CH20216._CH', 'ED6_DT26/CH20216P._CP'),
        ('ED6_DT26/CH20217._CH', 'ED6_DT26/CH20217P._CP'),
        ('ED6_DT26/CH20219._CH', 'ED6_DT26/CH20219P._CP'),
        ('ED6_DT07/CH00120._CH', 'ED6_DT07/CH00120P._CP'),
        ('ED6_DT07/CH00150._CH', 'ED6_DT07/CH00150P._CP'),
        ('ED6_DT07/CH00130._CH', 'ED6_DT07/CH00130P._CP'),
        ('ED6_DT07/CH00140._CH', 'ED6_DT07/CH00140P._CP'),
        ('ED6_DT07/CH00160._CH', 'ED6_DT07/CH00160P._CP'),
        ('ED6_DT07/CH00170._CH', 'ED6_DT07/CH00170P._CP'),
        ('ED6_DT27/CH04080._CH', 'ED6_DT27/CH04080P._CP'),
    ]

# id: 0x10001 offset: 0x202
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '黑发的少年',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '黑发的少年',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 12,
            chipIndex           = 12,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '黑发的少年',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 12,
            chipIndex           = 12,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '歼灭天使玲',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 25,
            chipIndex           = 25,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '剑帝莱维',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 26,
            chipIndex           = 26,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '怀斯曼教授',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 27,
            chipIndex           = 27,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10002 offset: 0x2C2
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            name        = '',
            x           = 33810,
            z           = 0,
            y           = 140000,
            word_0C     = 0x00B4,
            word_0E     = 0x0006,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x041D,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 68690,
            z           = 0,
            y           = 59150,
            word_0C     = 0x00B4,
            word_0E     = 0x0006,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x041D,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 43770,
            z           = 0,
            y           = 56260,
            word_0C     = 0x00B4,
            word_0E     = 0x0006,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x041D,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 40910,
            z           = 0,
            y           = 29220,
            word_0C     = 0x00B4,
            word_0E     = 0x0006,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x041D,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10003 offset: 0x332
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = -30680,
            y           = 0,
            z           = 53220,
            range       = -27120,
            dword_10    = 0x000007D0,
            dword_14    = 0x0000DC64,
            dword_18    = 0x00000000,
            dword_1C    = 0x0000000D,
        ),
        ScenaEventData(
            x           = 19040,
            y           = -1000,
            z           = 143410,
            range       = 3000,
            dword_10    = 0x00000BB8,
            dword_14    = 0x00000000,
            dword_18    = 0x00000040,
            dword_1C    = 0x00000011,
        ),
    )

# id: 0x10004 offset: 0x372
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -33630,
            triggerZ            = 0,
            triggerY            = 11690,
            triggerRange        = 1000,
            actorX              = -33630,
            actorZ              = 1000,
            actorY              = 11690,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0010,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x396
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x6C),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3AE',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0381, 7, 0x1C0F)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3AE',
    )

    Event(0, func_02_42A)

    def _loc_3AE(): pass

    label('loc_3AE')

    Return()

# id: 0x0001 offset: 0x3AF
@scena.Code('func_01_3AF')
def func_01_3AF():
    If(
        (
            (Expr.PushValueByIndex, 0x29),
            (Expr.PushLong, 0x421),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3C4',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_3C4(): pass

    label('loc_3C4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0381, 7, 0x1C0F)),
            Expr.Return,
        ),
        'loc_3D4',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x51),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_3D4(): pass

    label('loc_3D4')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_429',
    )

    LoadEffect(0x00, 'map\\\\mp027_00.eff')
    PlayEffect(0x00, 0x00, 0x00FF, -33630, 1000, 11690, 0, 0, 0, 1300, 1300, 1300, 0x00FF, 0, 0, 0, 0)

    def _loc_429(): pass

    label('loc_429')

    Return()

# id: 0x0002 offset: 0x42A
@scena.Code('func_02_42A')
def func_02_42A():
    Call(0, 0x0003)
    Call(0, 0x000A)

    Return()

# id: 0x0003 offset: 0x433
@scena.Code('func_03_433')
def func_03_433():
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
        'loc_44A',
    )

    Call(0, 0x000E)
    Call(0, 0x000F)

    def _loc_44A(): pass

    label('loc_44A')

    ChrSetPos(0x0008, -28400, 0, 69850, 270)
    ChrClearFlags(0x0008, 0x0080)
    ChrSetFlags(0x0008, 0x0002)
    ChrSetFlags(0x0008, 0x0040)
    ChrClearFlags(0x0008, 0x0001)
    ChrSetChipByIndex(0x0008, 10)
    ChrSetSubChip(0x0008, 48)
    ChrSetPos(0x0101, -28090, 20, 57140, 0)
    ChrSetPos(0x0109, -29480, 20, 57110, 0)
    ChrSetPos(0x00F8, -28090, 0, 55760, 0)
    ChrSetPos(0x00F9, -29480, 0, 55760, 0)
    CameraMove(-28600, 0, 57330, 0)
    OP_67(0, 8580, -10000, 0)
    CameraSetDistance(2580, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    FadeIn(1000, 0)
    OP_0D()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    OP_20(0x00000BB8)

    @scena.Lambda('lambda_052B')
    def lambda_052B():
        CameraMove(-29160, 20, 70000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_052B)

    @scena.Lambda('lambda_0543')
    def lambda_0543():
        OP_67(0, 6570, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0109, 0x0002, lambda_0543)

    @scena.Lambda('lambda_055B')
    def lambda_055B():
        CameraSetDistance(2580, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_055B)

    @scena.Lambda('lambda_056B')
    def lambda_056B():
        OP_6E(278, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_056B)

    WaitForThreadExit(0x0101, 0x0000)
    Sleep(1000)

    Fade(500)
    CameraMove(-29050, 10, 62510, 0)
    OP_67(0, 6100, -10000, 0)
    CameraSetDistance(2410, 0)
    OP_6E(393, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x0101,
        (
            '#0010321375V#3S#1020F约修亚！？',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()
    PlayBGM(48)
    Sleep(500)

    @scena.Lambda('lambda_0601')
    def lambda_0601():
        ChrWalkTo(0x0101, -28920, 20, 69300, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_0601)

    Sleep(500)

    Fade(500)
    CameraMove(-28990, 20, 70000, 0)
    OP_67(0, 6570, -10000, 0)
    CameraSetDistance(2600, 0)
    OP_6E(290, 0)
    OP_0D()
    WaitForThreadExit(0x0101, 0x0000)
    Fade(500)
    ChrSetSubChip(0x0101, 0)
    ChrSetChipByIndex(0x0101, 11)
    OP_0D()
    Sleep(500)

    @scena.Lambda('lambda_0675')
    def lambda_0675():
        OP_9E(0x00FE, 0, 10, 1000, 1000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0675)

    CreateThread(0x0109, 0x01, 0x00, func_04_12E1)
    Sleep(70)

    CreateThread(0x00F8, 0x01, 0x00, func_05_12FD)
    Sleep(70)

    CreateThread(0x00F9, 0x01, 0x00, func_06_1319)

    ChrTalk(
        0x0101,
        (
            '#0010321376V#1023F#6P约修亚！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010321377V喂，我在跟你说话啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_06F3')
    def lambda_06F3():
        OP_9E(0x00FE, 0, 10, 1000, 1000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_06F3)

    Sleep(1500)

    ChrTalk(
        0x0101,
        (
            '#0010321378V#1027F#6P为、为什么身体\n',
            '会冷成这样……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010321379V#1014F起来……快起来啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x00F8, 0x0001)
    WaitForThreadExit(0x00F9, 0x0001)

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_7AA',
    )

    ChrTalk(
        0x0105,
        (
            '#0060321380V#049F#6P怎、怎么会……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_7AA(): pass

    label('loc_7AA')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_7DE',
    )

    ChrTalk(
        0x0107,
        (
            '#0070321381V#065F#6P哥、哥哥……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_7DE(): pass

    label('loc_7DE')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_814',
    )

    ChrTalk(
        0x0103,
        (
            '#0030321382V#522F#6P……骗人………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_814(): pass

    label('loc_814')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_842',
    )

    ChrTalk(
        0x0106,
        (
            '#0050321383V#552F#6P呜……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_842(): pass

    label('loc_842')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_880',
    )

    ChrTalk(
        0x0104,
        (
            '#0040321384V#032F#6P……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_880(): pass

    label('loc_880')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_8BE',
    )

    ChrTalk(
        0x0108,
        (
            '#0080321385V#572F#6P……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_8BE(): pass

    label('loc_8BE')

    ChrTalk(
        0x0008,
        (
            '#0020321386V#2P#40W……呜……………',
            TxtCtl.Enter,
        ),
    )

    OP_9E(0x0008, 15, 0, 300, 3000)
    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0109, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_959',
    )

    OP_62(0x00F8, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_997')

    def _loc_959(): pass

    label('loc_959')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_980',
    )

    OP_62(0x00F8, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_997')

    def _loc_980(): pass

    label('loc_980')

    OP_62(0x00F8, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    def _loc_997(): pass

    label('loc_997')

    Sleep(50)

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_9C3',
    )

    OP_62(0x00F9, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_A01')

    def _loc_9C3(): pass

    label('loc_9C3')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_9EA',
    )

    OP_62(0x00F9, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_A01')

    def _loc_9EA(): pass

    label('loc_9EA')

    OP_62(0x00F9, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    def _loc_A01(): pass

    label('loc_A01')

    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010321387V#1023F#6P约修亚！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0020321388V#2P#40W……艾……艾丝蒂尔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0020321389V#2P#40W为什么你……\n',
            '……会在这种地方……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010321390V#1027F#6P太、太好了……\n',
            '原来你……没事……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010321391V#1005F你等着，马上替你治疗──',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0109,
        (
            '#0180321392V#1069F#6P不行！　快离开！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    LoadEffect(0x02, 'map\\\\mp009_00.eff')

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    @scena.Lambda('lambda_0B66')
    def lambda_0B66():
        CameraSetDistance(2400, 500)

        ExitThread()

    DispatchAsync(0x0109, 0x0003, lambda_0B66)

    OP_20(0x00000190)
    PlaySE(163, 0x00, 0x64)

    @scena.Lambda('lambda_0B80')
    def lambda_0B80():
        ChrJumpTo(0x00FE, -28700, 0, 70300, 500, 5000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0B80)

    Sleep(50)

    ChrClearFlags(0x0008, 0x0002)
    ChrSetFlags(0x0008, 0x0001)
    ChrSetChipByIndex(0x0008, 14)
    ChrSetSubChip(0x0008, 1)
    ChrSetDirection(0x0008, 180, 0)
    WaitForThreadExit(0x0008, 0x0001)
    PlaySE(501, 0x00, 0x64)
    ChrSetChipByIndex(0x0101, 65535)
    ChrSetSubChip(0x0101, 0)
    ChrSetChipByIndex(0x0008, 14)

    @scena.Lambda('lambda_0BD7')
    def lambda_0BD7():
        OP_99(0x0008, 0x01, 0x0B, 4000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0BD7)

    ChrSetChipByIndex(0x0101, 16)
    ChrClearFlags(0x0008, 0x0002)
    ChrSetFlags(0x0008, 0x0001)
    Sleep(100)

    PlayEffect(0x02, 0x01, 0x0101, 0, 500, 500, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlaySE(214, 0x00, 0x64)

    @scena.Lambda('lambda_0C35')
    def lambda_0C35():
        OP_9E(0x00FE, 20, 0, 2000, 2500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0C35)

    @scena.Lambda('lambda_0C4F')
    def lambda_0C4F():
        OP_9E(0x00FE, 20, 0, 2000, 2500)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_0C4F)

    WaitForThreadExit(0x0008, 0x0001)
    ChrSetChipByIndex(0x0008, 10)
    ChrSetSubChip(0x0008, 0)
    Sleep(50)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    CreateThread(0x0109, 0x01, 0x00, func_07_1335)
    Sleep(50)

    CreateThread(0x00F8, 0x01, 0x00, func_08_1351)
    Sleep(50)

    CreateThread(0x00F9, 0x01, 0x00, func_09_136D)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010321393V#1021F#6P呜……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0CCD')
    def lambda_0CCD():
        CameraMove(-28920, 0, 70500, 500)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0CCD)

    @scena.Lambda('lambda_0CE5')
    def lambda_0CE5():
        OP_67(0, 6800, -10000, 500)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_0CE5)

    @scena.Lambda('lambda_0CFD')
    def lambda_0CFD():
        CameraSetDistance(2700, 500)

        ExitThread()

    DispatchAsync(0x0009, 0x0003, lambda_0CFD)

    PlaySE(163, 0x00, 0x64)
    ChrSetChipByIndex(0x0008, 10)
    ChrSetSubChip(0x0008, 0)

    @scena.Lambda('lambda_0D1C')
    def lambda_0D1C():
        ChrJumpTo(0x00FE, -28920, 0, 72980, 500, 6000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0D1C)

    @scena.Lambda('lambda_0D3A')
    def lambda_0D3A():
        ChrMoveTo(0x00FE, -28920, 0, 68300, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0D3A)

    WaitForThreadExit(0x0109, 0x0003)
    Sleep(1000)

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_D8E',
    )

    ChrTalk(
        0x0105,
        (
            '#0060321394V#043F#6P咦……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E30')

    def _loc_D8E(): pass

    label('loc_D8E')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_DC9',
    )

    ChrTalk(
        0x0107,
        (
            '#0070321395V#065F#6P哥、哥哥……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E30')

    def _loc_DC9(): pass

    label('loc_DC9')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_DFE',
    )

    ChrTalk(
        0x0103,
        (
            '#0030321396V#024F#6P什……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E30')

    def _loc_DFE(): pass

    label('loc_DFE')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_E30',
    )

    ChrTalk(
        0x0106,
        (
            '#0050321397V#054F#6P什……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_E30(): pass

    label('loc_E30')

    ChrTalk(
        0x0101,
        (
            '#0010321398V#1020F#6P约、约修亚……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0020321399V#2P……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(500)
    CameraMove(-28920, 0, 71980, 0)
    OP_67(0, 6040, -10000, 0)
    CameraSetDistance(2770, 0)
    OP_6C(0, 0)
    OP_6E(290, 0)
    ChrSetFlags(0x0008, 0x0002)
    ChrSetSubChip(0x0008, 6)
    OP_0D()
    PlaySE(300, 0x00, 0x50)
    PlaySE(273, 0x00, 0x50)

    @scena.Lambda('lambda_0EE6')
    def lambda_0EE6():
        OP_99(0x00FE, 0x20, 0x21, 2500)
        Yield()

        Jump('lambda_0EE6')

    DispatchAsync2(0x0008, 0x0001, lambda_0EE6)

    Sleep(1000)

    TerminateThread(0x0008, 0x01)
    Fade(300)
    OP_99(0x0008, 0x22, 0x25, 1000)
    Fade(500)
    ChrSetSubChip(0x0008, 30)
    OP_0D()
    PlaySE(156, 0x00, 0x64)
    Sleep(500)

    NpcTalk(
        0x0008,
        '黑发的人偶',
        (
            '#0020321400V#5P#1140F……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010321401V#1020F#6P#4S！！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0109,
        (
            '#0180321402V#1069F#6P人偶……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_FDC',
    )

    ChrTalk(
        0x0104,
        (
            '#0040321403V#530F#6P……果然没错吗！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_FDC(): pass

    label('loc_FDC')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1010',
    )

    ChrTalk(
        0x0108,
        (
            '#0080321404V#077F#6P小花招……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1010(): pass

    label('loc_1010')

    Sleep(100)

    Fade(500)
    OP_6C(315000, 0)

    @scena.Lambda('lambda_1029')
    def lambda_1029():
        CameraMove(-29050, 20, 68500, 0)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1029)

    @scena.Lambda('lambda_1041')
    def lambda_1041():
        CameraSetDistance(2800, 0)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1041)

    ChrClearFlags(0x0008, 0x0002)
    ChrSetDirection(0x0008, 180, 0)
    ChrSetSubChip(0x0008, 3)
    OP_0D()
    ChrSetRGBAMask(0x0009, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x000A, 255, 255, 255, 0, 0)
    ChrSetFlags(0x0009, 0x0004)
    ChrSetFlags(0x000A, 0x0004)
    ChrSetPos(0x0009, -32509, 3000, 64540, 45)
    ChrSetPos(0x000A, -24330, 3000, 64720, 315)
    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x000A, 0x0080)

    @scena.Lambda('lambda_10AF')
    def lambda_10AF():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_10AF)

    @scena.Lambda('lambda_10C1')
    def lambda_10C1():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_10C1)

    @scena.Lambda('lambda_10D3')
    def lambda_10D3():
        ChrMoveTo(0x00FE, -32509, 0, 64540, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_10D3)

    PlaySE(529, 0x00, 0x64)
    Sleep(200)

    @scena.Lambda('lambda_10F8')
    def lambda_10F8():
        ChrMoveTo(0x000A, -24330, 0, 64720, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_10F8)

    PlaySE(529, 0x00, 0x64)
    WaitForThreadExit(0x0009, 0x0001)
    PlaySE(164, 0x00, 0x64)
    WaitForThreadExit(0x000A, 0x0001)
    PlaySE(164, 0x00, 0x64)

    @scena.Lambda('lambda_112C')
    def lambda_112C():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0109, 0x0001, lambda_112C)

    Sleep(100)

    @scena.Lambda('lambda_113F')
    def lambda_113F():
        ChrSetDirection(0x00FE, 225, 400)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_113F)

    Sleep(100)

    ChrSetDirection(0x00F8, 135, 400)
    ChrSetChipByIndex(0x0109, 42)

    Switch(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            Expr.Return,
        ),
        (0x00000002, 'loc_1179'),
        (0x00000005, 'loc_1181'),
        (0x00000003, 'loc_1189'),
        (0x00000004, 'loc_1191'),
        (0x00000006, 'loc_1199'),
        (0x00000007, 'loc_11A1'),
        (-1, 'loc_11A9'),
    )

    def _loc_1179(): pass

    label('loc_1179')

    ChrSetChipByIndex(0x00F8, 36)

    Jump('loc_11A9')

    def _loc_1181(): pass

    label('loc_1181')

    ChrSetChipByIndex(0x00F8, 37)

    Jump('loc_11A9')

    def _loc_1189(): pass

    label('loc_1189')

    ChrSetChipByIndex(0x00F8, 38)

    Jump('loc_11A9')

    def _loc_1191(): pass

    label('loc_1191')

    ChrSetChipByIndex(0x00F8, 39)

    Jump('loc_11A9')

    def _loc_1199(): pass

    label('loc_1199')

    ChrSetChipByIndex(0x00F8, 40)

    Jump('loc_11A9')

    def _loc_11A1(): pass

    label('loc_11A1')

    ChrSetChipByIndex(0x00F8, 41)

    Jump('loc_11A9')

    def _loc_11A9(): pass

    label('loc_11A9')

    Switch(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            Expr.Return,
        ),
        (0x00000002, 'loc_11CA'),
        (0x00000005, 'loc_11D2'),
        (0x00000003, 'loc_11DA'),
        (0x00000004, 'loc_11E2'),
        (0x00000006, 'loc_11EA'),
        (0x00000007, 'loc_11F2'),
        (-1, 'loc_11FA'),
    )

    def _loc_11CA(): pass

    label('loc_11CA')

    ChrSetChipByIndex(0x00F9, 36)

    Jump('loc_11FA')

    def _loc_11D2(): pass

    label('loc_11D2')

    ChrSetChipByIndex(0x00F9, 37)

    Jump('loc_11FA')

    def _loc_11DA(): pass

    label('loc_11DA')

    ChrSetChipByIndex(0x00F9, 38)

    Jump('loc_11FA')

    def _loc_11E2(): pass

    label('loc_11E2')

    ChrSetChipByIndex(0x00F9, 39)

    Jump('loc_11FA')

    def _loc_11EA(): pass

    label('loc_11EA')

    ChrSetChipByIndex(0x00F9, 40)

    Jump('loc_11FA')

    def _loc_11F2(): pass

    label('loc_11F2')

    ChrSetChipByIndex(0x00F9, 41)

    Jump('loc_11FA')

    def _loc_11FA(): pass

    label('loc_11FA')

    Sleep(500)

    PlayBGM(27)
    Sleep(500)

    @scena.Lambda('lambda_120C')
    def lambda_120C():
        CameraMove(-28860, 20, 68620, 300)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_120C)

    @scena.Lambda('lambda_1224')
    def lambda_1224():
        CameraSetDistance(2130, 300)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1224)

    ChrClearFlags(0x0008, 0x0002)
    ChrSetChipByIndex(0x0008, 13)

    @scena.Lambda('lambda_123E')
    def lambda_123E():
        ChrWalkTo(0x00FE, -28910, 20, 70120, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_123E)

    Sleep(50)

    ChrSetChipByIndex(0x0009, 13)

    @scena.Lambda('lambda_1263')
    def lambda_1263():
        ChrWalkTo(0x00FE, -30280, 20, 67370, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_1263)

    ChrSetChipByIndex(0x000A, 13)

    @scena.Lambda('lambda_1283')
    def lambda_1283():
        ChrWalkTo(0x00FE, -27030, 20, 67050, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_1283)

    Sleep(60)

    OP_94(0x00, 0x000A, 0x0000, 0x000007D0, 0x00001B58, 0x00)
    WaitForThreadExit(0x0101, 0x0001)
    TerminateThread(0x0008, 0x01)
    TerminateThread(0x0009, 0x01)
    TerminateThread(0x000A, 0x01)
    Battle(0x00000421, 0x00000000, 0x01, 0x0000, 0xFF)
    ChrSetStatus(0x00FF, 0xF9, 0)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000001, 'loc_12DB'),
        (-1, 'loc_12E0'),
    )

    def _loc_12DB(): pass

    label('loc_12DB')

    OP_B4(0x00)

    Jump('loc_12E0')

    def _loc_12E0(): pass

    label('loc_12E0')

    Return()

# id: 0x0004 offset: 0x12E1
@scena.Code('func_04_12E1')
def func_04_12E1():
    ChrWalkTo(0x00FE, -28670, 20, 67030, 5000, 0x00)
    ChrSetDirection(0x00FE, 0, 400)

    Return()

# id: 0x0005 offset: 0x12FD
@scena.Code('func_05_12FD')
def func_05_12FD():
    ChrWalkTo(0x00FE, -27380, 20, 68040, 5000, 0x00)
    ChrSetDirection(0x00FE, 315, 400)

    Return()

# id: 0x0006 offset: 0x1319
@scena.Code('func_06_1319')
def func_06_1319():
    ChrWalkTo(0x00FE, -30190, 20, 68090, 5000, 0x00)
    ChrSetDirection(0x00FE, 45, 400)

    Return()

# id: 0x0007 offset: 0x1335
@scena.Code('func_07_1335')
def func_07_1335():
    ChrSetDirection(0x00FE, 0, 0)
    ChrMoveTo(0x00FE, -28670, 20, 66500, 5000, 0x00)

    Return()

# id: 0x0008 offset: 0x1351
@scena.Code('func_08_1351')
def func_08_1351():
    ChrSetDirection(0x00FE, 0, 0)
    ChrMoveTo(0x00FE, -27380, 20, 67500, 5000, 0x00)

    Return()

# id: 0x0009 offset: 0x136D
@scena.Code('func_09_136D')
def func_09_136D():
    ChrSetDirection(0x00FE, 0, 0)
    ChrMoveTo(0x00FE, -30190, 20, 67500, 5000, 0x00)

    Return()

# id: 0x000A offset: 0x1389
@scena.Code('func_0A_1389')
def func_0A_1389():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    OP_0D()
    TerminateThread(0x0101, 0x01)
    TerminateThread(0x0101, 0x02)
    TerminateThread(0x0008, 0x01)
    TerminateThread(0x0009, 0x01)
    TerminateThread(0x000A, 0x01)
    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x000A, 0x0080)
    ChrSetPos(0x0008, -32200, 0, 69470, 0)
    ChrSetPos(0x0009, -28040, 0, 65390, 0)
    ChrSetPos(0x000A, -24030, 0, 69690, 0)
    ChrSetFlags(0x0008, 0x0002)
    ChrSetFlags(0x0009, 0x0002)
    ChrSetFlags(0x000A, 0x0002)
    ChrSetChipByIndex(0x0008, 15)
    ChrSetSubChip(0x0008, 3)
    ChrSetChipByIndex(0x0009, 15)
    ChrSetSubChip(0x0009, 1)
    ChrSetChipByIndex(0x000A, 15)
    ChrSetSubChip(0x000A, 7)
    ChrClearFlags(0x0008, 0x0001)
    ChrClearFlags(0x0009, 0x0001)
    ChrClearFlags(0x000A, 0x0001)
    Sleep(500)

    LoadChip('ED6_DT26/CH20498._CH', 'ED6_DT26/CH20498P._CP', 0)
    ChrSetPos(0x0101, -27400, 20, 70790, 90)
    ChrSetPos(0x0109, -28810, 20, 68890, 180)
    ChrSetPos(0x00F8, -27120, 20, 69000, 135)
    ChrSetPos(0x00F9, -28990, 20, 70710, 270)
    ChrSetSubChip(0x0101, 0)
    ChrSetSubChip(0x0109, 0)
    ChrSetSubChip(0x00F8, 0)
    ChrSetSubChip(0x00F9, 0)
    ChrSetChipByIndex(0x0101, 16)
    ChrSetChipByIndex(0x0109, 42)

    Switch(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            Expr.Return,
        ),
        (0x00000002, 'loc_14BA'),
        (0x00000005, 'loc_14C2'),
        (0x00000003, 'loc_14CA'),
        (0x00000004, 'loc_14D2'),
        (0x00000006, 'loc_14DA'),
        (0x00000007, 'loc_14E2'),
        (-1, 'loc_14EA'),
    )

    def _loc_14BA(): pass

    label('loc_14BA')

    ChrSetChipByIndex(0x00F8, 36)

    Jump('loc_14EA')

    def _loc_14C2(): pass

    label('loc_14C2')

    ChrSetChipByIndex(0x00F8, 37)

    Jump('loc_14EA')

    def _loc_14CA(): pass

    label('loc_14CA')

    ChrSetChipByIndex(0x00F8, 38)

    Jump('loc_14EA')

    def _loc_14D2(): pass

    label('loc_14D2')

    ChrSetChipByIndex(0x00F8, 39)

    Jump('loc_14EA')

    def _loc_14DA(): pass

    label('loc_14DA')

    ChrSetChipByIndex(0x00F8, 40)

    Jump('loc_14EA')

    def _loc_14E2(): pass

    label('loc_14E2')

    ChrSetChipByIndex(0x00F8, 41)

    Jump('loc_14EA')

    def _loc_14EA(): pass

    label('loc_14EA')

    Switch(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            Expr.Return,
        ),
        (0x00000002, 'loc_150B'),
        (0x00000005, 'loc_1513'),
        (0x00000003, 'loc_151B'),
        (0x00000004, 'loc_1523'),
        (0x00000006, 'loc_152B'),
        (0x00000007, 'loc_1533'),
        (-1, 'loc_153B'),
    )

    def _loc_150B(): pass

    label('loc_150B')

    ChrSetChipByIndex(0x00F9, 36)

    Jump('loc_153B')

    def _loc_1513(): pass

    label('loc_1513')

    ChrSetChipByIndex(0x00F9, 37)

    Jump('loc_153B')

    def _loc_151B(): pass

    label('loc_151B')

    ChrSetChipByIndex(0x00F9, 38)

    Jump('loc_153B')

    def _loc_1523(): pass

    label('loc_1523')

    ChrSetChipByIndex(0x00F9, 39)

    Jump('loc_153B')

    def _loc_152B(): pass

    label('loc_152B')

    ChrSetChipByIndex(0x00F9, 40)

    Jump('loc_153B')

    def _loc_1533(): pass

    label('loc_1533')

    ChrSetChipByIndex(0x00F9, 41)

    Jump('loc_153B')

    def _loc_153B(): pass

    label('loc_153B')

    CameraMove(-29090, 20, 70550, 0)
    OP_67(0, 6590, -10000, 0)
    CameraSetDistance(2410, 0)
    OP_6C(315000, 0)
    OP_6E(323, 0)
    FadeIn(2000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010321405V#1022F#5P哈呼呼……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0109,
        (
            '#0180321406V#1070F#5P唔……\n',
            '实在很棘手呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(123, 0x00, 0x64)
    Sleep(500)

    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0109, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1642',
    )

    OP_62(0x00F8, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_1680')

    def _loc_1642(): pass

    label('loc_1642')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1669',
    )

    OP_62(0x00F8, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_1680')

    def _loc_1669(): pass

    label('loc_1669')

    OP_62(0x00F8, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    def _loc_1680(): pass

    label('loc_1680')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_16A7',
    )

    OP_62(0x00F9, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_16E5')

    def _loc_16A7(): pass

    label('loc_16A7')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_16CE',
    )

    OP_62(0x00F9, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_16E5')

    def _loc_16CE(): pass

    label('loc_16CE')

    OP_62(0x00F9, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    def _loc_16E5(): pass

    label('loc_16E5')

    Sleep(500)

    PlayBGM(90)
    Sleep(500)

    @scena.Lambda('lambda_16F7')
    def lambda_16F7():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_16F7)

    Sleep(50)

    @scena.Lambda('lambda_170A')
    def lambda_170A():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0109, 0x0001, lambda_170A)

    Sleep(50)

    @scena.Lambda('lambda_171D')
    def lambda_171D():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_171D)

    Sleep(50)

    ChrSetDirection(0x00F8, 0, 400)
    Fade(500)
    MapSetFlags(0x00000010)
    OP_11(0x00, 0x00, 0x00, 28100, 37500, 0)
    ChrSetChipByIndex(0x000D, 27)
    ChrSetSubChip(0x000D, 0)
    ChrSetFlags(0x000D, 0x0800)
    ChrSetPos(0x000D, -29000, 500, 85950, 180)
    ChrSetPos(0x000B, -28040, 500, 84990, 180)
    ChrSetPos(0x000C, -30050, 500, 84890, 180)
    ChrClearFlags(0x000D, 0x0080)
    ChrClearFlags(0x000B, 0x0080)
    ChrClearFlags(0x000C, 0x0080)
    CameraMove(-29070, 0, 77150, 0)
    OP_67(0, 4500, -10000, 0)
    CameraSetDistance(3160, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)

    @scena.Lambda('lambda_17DF')
    def lambda_17DF():
        CameraMove(-28990, 500, 84290, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_17DF)

    WaitForThreadExit(0x0101, 0x0001)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010301311V#1020F#5P啊……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x000B,
        '少女',
        (
            '#0220321408V#5P嘻嘻……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x000C,
        '青年',
        (
            '#0140321409V#5P……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x000D,
        '坐着的男性',
        (
            '#0150321410V#5P哈哈，察觉到是冒牌货\n',
            '似乎稍微晚了一点呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150321411V这次的游戏\n',
            '是我赢了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetFlags(0x000D, 0x0002)
    ChrSetChipByIndex(0x000D, 0)
    ChrSetSubChip(0x000D, 0)
    Sleep(300)

    PlaySE(188, 0x00, 0x64)
    ChrSetSubChip(0x000D, 1)
    Sleep(1000)

    Fade(500)
    ChrClearFlags(0x000D, 0x0002)
    ChrSetChipByIndex(0x000D, 27)
    ChrSetSubChip(0x000D, 0)
    ChrClearFlags(0x000D, 0x0800)
    ChrSetDirection(0x0101, 0, 0)
    ChrSetDirection(0x0109, 0, 0)
    ChrSetDirection(0x00F8, 0, 0)
    ChrSetDirection(0x00F9, 0, 0)
    CameraMove(-28620, 20, 74760, 0)
    OP_67(0, 5020, -10000, 0)
    CameraSetDistance(2260, 0)
    OP_6C(315000, 0)
    OP_6E(364, 0)
    OP_0D()
    OP_B0(0x0007, 0x1E)
    OP_6F(0x0007, 0)
    OP_70(0x0007, 30)
    PlaySE(304, 0x00, 0x64)
    OP_73(0x0007)
    OP_62(0x0101, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0109, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x00F8, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x00F9, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010321412V#1005F#5P什…什么…！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0109,
        (
            '#0180321413V#1069F#5P糟糕……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1A44')
    def lambda_1A44():
        CameraMove(-28950, 20, 70480, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_1A44)

    LoadEffect(0x01, 'map\\mp089_00.eff')
    PlayEffect(0x01, 0x00, 0x00FF, -28170, 0, 69720, 0, 0, 0, 900, 900, 900, 0x00FF, 0, 0, 0, 0)
    PlaySE(960, 0x00, 0x64)
    Sleep(2000)

    OP_11(0xFF, 0xFF, 0xFF, 0, 120000, 0)
    MapSetFlags(0x00000010)
    OP_12(0x00000000, 0x00007530, 0x00000FA0)
    ChrSetSubChip(0x0101, 0)
    ChrSetSubChip(0x0109, 0)
    ChrSetSubChip(0x00F8, 0)
    ChrSetSubChip(0x00F9, 0)
    ChrSetChipByIndex(0x0101, 17)
    ChrSetChipByIndex(0x0109, 24)

    Switch(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            Expr.Return,
        ),
        (0x00000002, 'loc_1B09'),
        (0x00000005, 'loc_1B11'),
        (0x00000003, 'loc_1B19'),
        (0x00000004, 'loc_1B21'),
        (0x00000006, 'loc_1B29'),
        (0x00000007, 'loc_1B31'),
        (-1, 'loc_1B39'),
    )

    def _loc_1B09(): pass

    label('loc_1B09')

    ChrSetChipByIndex(0x00F8, 18)

    Jump('loc_1B39')

    def _loc_1B11(): pass

    label('loc_1B11')

    ChrSetChipByIndex(0x00F8, 19)

    Jump('loc_1B39')

    def _loc_1B19(): pass

    label('loc_1B19')

    ChrSetChipByIndex(0x00F8, 20)

    Jump('loc_1B39')

    def _loc_1B21(): pass

    label('loc_1B21')

    ChrSetChipByIndex(0x00F8, 21)

    Jump('loc_1B39')

    def _loc_1B29(): pass

    label('loc_1B29')

    ChrSetChipByIndex(0x00F8, 22)

    Jump('loc_1B39')

    def _loc_1B31(): pass

    label('loc_1B31')

    ChrSetChipByIndex(0x00F8, 23)

    Jump('loc_1B39')

    def _loc_1B39(): pass

    label('loc_1B39')

    Switch(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            Expr.Return,
        ),
        (0x00000002, 'loc_1B5A'),
        (0x00000005, 'loc_1B62'),
        (0x00000003, 'loc_1B6A'),
        (0x00000004, 'loc_1B72'),
        (0x00000006, 'loc_1B7A'),
        (0x00000007, 'loc_1B82'),
        (-1, 'loc_1B8A'),
    )

    def _loc_1B5A(): pass

    label('loc_1B5A')

    ChrSetChipByIndex(0x00F9, 18)

    Jump('loc_1B8A')

    def _loc_1B62(): pass

    label('loc_1B62')

    ChrSetChipByIndex(0x00F9, 19)

    Jump('loc_1B8A')

    def _loc_1B6A(): pass

    label('loc_1B6A')

    ChrSetChipByIndex(0x00F9, 20)

    Jump('loc_1B8A')

    def _loc_1B72(): pass

    label('loc_1B72')

    ChrSetChipByIndex(0x00F9, 21)

    Jump('loc_1B8A')

    def _loc_1B7A(): pass

    label('loc_1B7A')

    ChrSetChipByIndex(0x00F9, 22)

    Jump('loc_1B8A')

    def _loc_1B82(): pass

    label('loc_1B82')

    ChrSetChipByIndex(0x00F9, 23)

    Jump('loc_1B8A')

    def _loc_1B8A(): pass

    label('loc_1B8A')

    ChrTalk(
        0x0101,
        (
            '#0010321414V#1020F#6P啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1BE4',
    )

    ChrTalk(
        0x0108,
        (
            '#0080321415V#077F#6P……这家伙是！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1CC3')

    def _loc_1BE4(): pass

    label('loc_1BE4')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1C1D',
    )

    ChrTalk(
        0x0106,
        (
            '#0050321416V#057F#6P这家伙是……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1CC3')

    def _loc_1C1D(): pass

    label('loc_1C1D')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1C56',
    )

    ChrTalk(
        0x0103,
        (
            '#0030321417V#523F#6P这、这是……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1CC3')

    def _loc_1C56(): pass

    label('loc_1C56')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1C8B',
    )

    ChrTalk(
        0x0107,
        (
            '#0070321418V#065F#6P这是……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1CC3')

    def _loc_1C8B(): pass

    label('loc_1C8B')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1CC3',
    )

    ChrTalk(
        0x0105,
        (
            '#0060321419V#541F#6P难、难不成……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1CC3(): pass

    label('loc_1CC3')

    ChrTalk(
        0x0109,
        (
            '#0180321420V#1070F#6P呜……意识……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1CF2')
    def lambda_1CF2():
        OP_99(0x0101, 0x00, 0x03, 500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1CF2)

    Sleep(200)

    PlaySE(524, 0x00, 0x64)

    @scena.Lambda('lambda_1D0C')
    def lambda_1D0C():
        OP_99(0x0109, 0x00, 0x03, 500)

        ExitThread()

    DispatchAsync(0x0109, 0x0001, lambda_1D0C)

    Sleep(150)

    PlaySE(524, 0x00, 0x64)

    @scena.Lambda('lambda_1D26')
    def lambda_1D26():
        OP_99(0x00F8, 0x00, 0x03, 500)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_1D26)

    Sleep(230)

    PlaySE(524, 0x00, 0x64)

    @scena.Lambda('lambda_1D40')
    def lambda_1D40():
        OP_99(0x00F9, 0x00, 0x03, 500)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_1D40)

    Sleep(200)

    PlaySE(524, 0x00, 0x64)
    WaitForThreadExit(0x00F9, 0x0001)
    Sleep(2000)

    Fade(500)
    CameraMove(-29730, 0, 82210, 0)
    OP_67(0, 6670, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(224000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, -29400, 20, 70790, 0)
    ChrSetPos(0x0109, -30810, 20, 68890, 0)
    ChrSetPos(0x00F8, -29120, 20, 69000, 0)
    ChrSetPos(0x00F9, -30990, 20, 70710, 0)
    MapClearFlags(0x00000010)
    OP_0D()
    Sleep(500)

    StopEffect(0x00, 0x02)
    Fade(500)
    ChrSetChipByIndex(0x000D, 28)
    ChrSetSubChip(0x000D, 0)
    ChrSetPos(0x000D, -28900, 500, 85500, 180)
    OP_0D()
    Sleep(500)

    @scena.Lambda('lambda_1E1E')
    def lambda_1E1E():
        CameraMove(-29110, 0, 78890, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1E1E)

    @scena.Lambda('lambda_1E36')
    def lambda_1E36():
        OP_67(0, 5430, -10000, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1E36)

    ChrSetFlags(0x000D, 0x0004)
    ChrWalkTo(0x000D, -28840, 500, 84520, 1500, 0x00)
    ChrClearFlags(0x000D, 0x0004)

    @scena.Lambda('lambda_1E6C')
    def lambda_1E6C():
        ChrWalkTo(0x00FE, -28710, 0, 80310, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_1E6C)

    Sleep(500)

    @scena.Lambda('lambda_1E8C')
    def lambda_1E8C():
        ChrWalkTo(0x00FE, -27410, 0, 80670, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_1E8C)

    Sleep(100)

    @scena.Lambda('lambda_1EAC')
    def lambda_1EAC():
        ChrWalkTo(0x00FE, -30040, 0, 81100, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_1EAC)

    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x000D, 0x0001)
    Sleep(500)

    ChrTalk(
        0x000D,
        (
            '#0150321421V#1154F#4P游戏也太简单了\n',
            '不过你的反应相当令人开心。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150321422V#1151F就算是向你作为答谢好了……\n',
            '就让我招待你去个有趣的地方吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x00001388)
    FadeOut(2000, 0, -1)
    OP_0D()
    Sleep(5000)

    OP_6F(0x0007, 0)
    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x000A, 0x0080)
    ChrSetFlags(0x0008, 0x0080)
    ChrSetFlags(0x0009, 0x0080)
    ChrSetFlags(0x000A, 0x0080)
    ChrSetFlags(0x000D, 0x0080)
    ChrSetFlags(0x000B, 0x0080)
    ChrSetFlags(0x000C, 0x0080)
    ChrSetFlags(0x0101, 0x0080)
    ChrSetPos(0x0109, -28500, 20, 68210, 0)
    ChrSetPos(0x00F8, -27250, 20, 70600, 315)
    ChrSetPos(0x00F9, -30300, 20, 70530, 45)
    ChrSetFlags(0x0109, 0x0800)
    ChrSetFlags(0x00F8, 0x0800)
    ChrSetFlags(0x00F9, 0x0800)
    ChrSetSubChip(0x0109, 0)
    ChrSetSubChip(0x00F8, 0)
    ChrSetSubChip(0x00F9, 0)
    ChrSetChipByIndex(0x0109, 35)

    Switch(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            Expr.Return,
        ),
        (0x00000002, 'loc_2026'),
        (0x00000005, 'loc_202E'),
        (0x00000003, 'loc_2036'),
        (0x00000004, 'loc_203E'),
        (0x00000006, 'loc_2046'),
        (0x00000007, 'loc_204E'),
        (-1, 'loc_2056'),
    )

    def _loc_2026(): pass

    label('loc_2026')

    ChrSetChipByIndex(0x00F8, 29)

    Jump('loc_2056')

    def _loc_202E(): pass

    label('loc_202E')

    ChrSetChipByIndex(0x00F8, 30)

    Jump('loc_2056')

    def _loc_2036(): pass

    label('loc_2036')

    ChrSetChipByIndex(0x00F8, 31)

    Jump('loc_2056')

    def _loc_203E(): pass

    label('loc_203E')

    ChrSetChipByIndex(0x00F8, 32)

    Jump('loc_2056')

    def _loc_2046(): pass

    label('loc_2046')

    ChrSetChipByIndex(0x00F8, 33)

    Jump('loc_2056')

    def _loc_204E(): pass

    label('loc_204E')

    ChrSetChipByIndex(0x00F8, 34)

    Jump('loc_2056')

    def _loc_2056(): pass

    label('loc_2056')

    Switch(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            Expr.Return,
        ),
        (0x00000002, 'loc_2077'),
        (0x00000005, 'loc_207F'),
        (0x00000003, 'loc_2087'),
        (0x00000004, 'loc_208F'),
        (0x00000006, 'loc_2097'),
        (0x00000007, 'loc_209F'),
        (-1, 'loc_20A7'),
    )

    def _loc_2077(): pass

    label('loc_2077')

    ChrSetChipByIndex(0x00F9, 29)

    Jump('loc_20A7')

    def _loc_207F(): pass

    label('loc_207F')

    ChrSetChipByIndex(0x00F9, 30)

    Jump('loc_20A7')

    def _loc_2087(): pass

    label('loc_2087')

    ChrSetChipByIndex(0x00F9, 31)

    Jump('loc_20A7')

    def _loc_208F(): pass

    label('loc_208F')

    ChrSetChipByIndex(0x00F9, 32)

    Jump('loc_20A7')

    def _loc_2097(): pass

    label('loc_2097')

    ChrSetChipByIndex(0x00F9, 33)

    Jump('loc_20A7')

    def _loc_209F(): pass

    label('loc_209F')

    ChrSetChipByIndex(0x00F9, 34)

    Jump('loc_20A7')

    def _loc_20A7(): pass

    label('loc_20A7')

    CameraMove(-29040, 20, 70130, 0)
    OP_67(0, 6870, -10000, 0)
    CameraSetDistance(2530, 0)
    OP_6C(315000, 0)
    OP_6E(287, 0)
    FadeIn(2000, 0)
    OP_0D()
    Sleep(500)

    OP_9E(0x0109, 15, 0, 300, 3000)
    Sleep(500)

    ChrTalk(
        0x0109,
        (
            '#0180321423V#1070F#6P呜……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(200)

    Fade(500)

    @scena.Lambda('lambda_213C')
    def lambda_213C():
        OP_9E(0x00FE, 30, 0, 5000, 2000)
        Yield()

        Jump('lambda_213C')

    DispatchAsync2(0x0109, 0x0003, lambda_213C)

    ChrSetChipByIndex(0x0109, 24)
    ChrSetSubChip(0x0109, 3)
    OP_0D()
    OP_99(0x0109, 0x03, 0x00, 500)
    TerminateThread(0x0109, 0x03)
    Fade(250)
    ChrSetSubChip(0x0109, 0)
    ChrSetChipByIndex(0x0109, 65535)
    OP_0D()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_220B',
    )

    ChrTalk(
        0x0106,
        (
            '#0050291313V#056F#5P唔……',
            TxtCtl.Enter,
        ),
    )

    OP_9E(0x0106, 15, 0, 300, 3000)
    CloseMessageWindow()
    Sleep(200)

    Fade(500)

    @scena.Lambda('lambda_21CC')
    def lambda_21CC():
        OP_9E(0x00FE, 30, 0, 5000, 2000)
        Yield()

        Jump('lambda_21CC')

    DispatchAsync2(0x0106, 0x0003, lambda_21CC)

    ChrSetChipByIndex(0x0106, 19)
    ChrSetSubChip(0x0106, 3)
    OP_0D()
    OP_99(0x0106, 0x03, 0x00, 500)
    TerminateThread(0x0106, 0x03)
    Fade(250)
    ChrSetSubChip(0x0106, 0)
    ChrSetChipByIndex(0x0106, 65535)
    OP_0D()

    def _loc_220B(): pass

    label('loc_220B')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_22A1',
    )

    ChrTalk(
        0x0103,
        (
            '#0030321425V#522F#5P……啊………',
            TxtCtl.Enter,
        ),
    )

    OP_9E(0x0103, 15, 0, 300, 3000)
    CloseMessageWindow()
    Sleep(200)

    Fade(500)

    @scena.Lambda('lambda_2262')
    def lambda_2262():
        OP_9E(0x00FE, 30, 0, 5000, 2000)
        Yield()

        Jump('lambda_2262')

    DispatchAsync2(0x0103, 0x0003, lambda_2262)

    ChrSetChipByIndex(0x0103, 18)
    ChrSetSubChip(0x0103, 3)
    OP_0D()
    OP_99(0x0103, 0x03, 0x00, 500)
    TerminateThread(0x0103, 0x03)
    Fade(250)
    ChrSetSubChip(0x0103, 0)
    ChrSetChipByIndex(0x0103, 65535)
    OP_0D()

    def _loc_22A1(): pass

    label('loc_22A1')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2331',
    )

    ChrTalk(
        0x0108,
        (
            '#0080291316V#572F#5P唔……',
            TxtCtl.Enter,
        ),
    )

    OP_9E(0x0108, 15, 0, 300, 3000)
    CloseMessageWindow()
    Sleep(200)

    Fade(500)

    @scena.Lambda('lambda_22F2')
    def lambda_22F2():
        OP_9E(0x00FE, 30, 0, 5000, 2000)
        Yield()

        Jump('lambda_22F2')

    DispatchAsync2(0x0108, 0x0003, lambda_22F2)

    ChrSetChipByIndex(0x0108, 23)
    ChrSetSubChip(0x0108, 3)
    OP_0D()
    OP_99(0x0108, 0x03, 0x00, 500)
    TerminateThread(0x0108, 0x03)
    Fade(250)
    ChrSetSubChip(0x0108, 0)
    ChrSetChipByIndex(0x0108, 65535)
    OP_0D()

    def _loc_2331(): pass

    label('loc_2331')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_23C1',
    )

    ChrTalk(
        0x0105,
        (
            '#0060291315V#049F#5P啊……',
            TxtCtl.Enter,
        ),
    )

    OP_9E(0x0105, 15, 0, 300, 3000)
    CloseMessageWindow()
    Sleep(200)

    Fade(500)

    @scena.Lambda('lambda_2382')
    def lambda_2382():
        OP_9E(0x00FE, 30, 0, 5000, 2000)
        Yield()

        Jump('lambda_2382')

    DispatchAsync2(0x0105, 0x0003, lambda_2382)

    ChrSetChipByIndex(0x0105, 21)
    ChrSetSubChip(0x0105, 3)
    OP_0D()
    OP_99(0x0105, 0x03, 0x00, 500)
    TerminateThread(0x0105, 0x03)
    Fade(250)
    ChrSetSubChip(0x0105, 0)
    ChrSetChipByIndex(0x0105, 65535)
    OP_0D()

    def _loc_23C1(): pass

    label('loc_23C1')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2451',
    )

    ChrTalk(
        0x0107,
        (
            '#0070321428V#561F#5P哎……',
            TxtCtl.Enter,
        ),
    )

    OP_9E(0x0107, 15, 0, 300, 3000)
    CloseMessageWindow()
    Sleep(200)

    Fade(500)

    @scena.Lambda('lambda_2412')
    def lambda_2412():
        OP_9E(0x00FE, 30, 0, 5000, 2000)
        Yield()

        Jump('lambda_2412')

    DispatchAsync2(0x0107, 0x0003, lambda_2412)

    ChrSetChipByIndex(0x0107, 22)
    ChrSetSubChip(0x0107, 3)
    OP_0D()
    OP_99(0x0107, 0x03, 0x00, 500)
    TerminateThread(0x0107, 0x03)
    Fade(250)
    ChrSetSubChip(0x0107, 0)
    ChrSetChipByIndex(0x0107, 65535)
    OP_0D()

    def _loc_2451(): pass

    label('loc_2451')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_24E1',
    )

    ChrTalk(
        0x0104,
        (
            '#0040321429V#039F#5P唔……',
            TxtCtl.Enter,
        ),
    )

    OP_9E(0x0104, 15, 0, 300, 3000)
    CloseMessageWindow()
    Sleep(200)

    Fade(500)

    @scena.Lambda('lambda_24A2')
    def lambda_24A2():
        OP_9E(0x00FE, 30, 0, 5000, 2000)
        Yield()

        Jump('lambda_24A2')

    DispatchAsync2(0x0104, 0x0003, lambda_24A2)

    ChrSetChipByIndex(0x0104, 20)
    ChrSetSubChip(0x0104, 3)
    OP_0D()
    OP_99(0x0104, 0x03, 0x00, 500)
    TerminateThread(0x0104, 0x03)
    Fade(250)
    ChrSetSubChip(0x0104, 0)
    ChrSetChipByIndex(0x0104, 65535)
    OP_0D()

    def _loc_24E1(): pass

    label('loc_24E1')

    Sleep(500)

    ChrClearFlags(0x0109, 0x0800)
    ChrClearFlags(0x00F8, 0x0800)
    ChrClearFlags(0x00F9, 0x0800)

    @scena.Lambda('lambda_24FB')
    def lambda_24FB():
        ChrSetDirection(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_24FB)

    Sleep(100)

    ChrSetDirection(0x00F8, 270, 400)

    ChrTalk(
        0x0109,
        (
            '#0180321430V#1068F#6P真、真是不得了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180321431V#1063F艾丝蒂尔，你没事吗──',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0109, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    PlayBGM(81)
    Sleep(500)

    OP_62(0x0109, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    ChrSetDirection(0x0109, 90, 600)
    ChrSetDirection(0x0109, 180, 600)
    Sleep(500)

    ChrSetDirection(0x0109, 270, 600)
    Sleep(500)

    ChrSetDirection(0x0109, 180, 600)
    Fade(500)
    ChrSetSubChip(0x00F8, 0)
    ChrSetChipByIndex(0x00F8, 65535)
    ChrSetSubChip(0x00F9, 0)
    ChrSetChipByIndex(0x00F9, 65535)
    OP_0D()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2681',
    )

    ChrTurnDirection(0x0107, 0x0109, 400)

    ChrTalk(
        0x0107,
        (
            '#0070321432V#065F怎么了……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0109,
        (
            '#0180321433V#1069F#5P艾丝蒂尔！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180321434V#1067F喂、喂，开玩笑吧！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0107, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    Jump('loc_2920')

    def _loc_2681(): pass

    label('loc_2681')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2727',
    )

    ChrTurnDirection(0x0105, 0x0109, 400)

    ChrTalk(
        0x0105,
        (
            '#0060321435V#043F……怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0109,
        (
            '#0180321433V#1069F#5P艾丝蒂尔！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180321434V#1067F喂、喂，开玩笑吧！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0105, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    Jump('loc_2920')

    def _loc_2727(): pass

    label('loc_2727')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_27D1',
    )

    ChrTurnDirection(0x0103, 0x0101, 400)

    ChrTalk(
        0x0103,
        (
            '#0030321438V#522F怎、怎么了……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0109,
        (
            '#0180321433V#1069F#5P艾丝蒂尔！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180321434V#1067F喂、喂，开玩笑吧！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0103, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    Jump('loc_2920')

    def _loc_27D1(): pass

    label('loc_27D1')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_287B',
    )

    ChrTurnDirection(0x0106, 0x0109, 400)

    ChrTalk(
        0x0106,
        (
            '#0050321441V#552F怎么……怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0109,
        (
            '#0180321433V#1069F#5P艾丝蒂尔！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180321434V#1067F喂、喂，开玩笑吧！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0106, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    Jump('loc_2920')

    def _loc_287B(): pass

    label('loc_287B')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2920',
    )

    ChrTurnDirection(0x0104, 0x0109, 400)

    ChrTalk(
        0x0104,
        (
            '#0040321444V#033F怎么回事……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0109,
        (
            '#0180321433V#1069F#5P艾丝蒂尔！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180321434V#1067F喂、喂，开玩笑吧！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0104, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    def _loc_2920(): pass

    label('loc_2920')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2942',
    )

    OP_62(0x00F8, 0x00000000, 2300, 0x28, 0x2B, 0x00000064, 0x03)

    Jump('loc_2976')

    def _loc_2942(): pass

    label('loc_2942')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2964',
    )

    OP_62(0x00F8, 0x00000000, 1700, 0x28, 0x2B, 0x00000064, 0x03)

    Jump('loc_2976')

    def _loc_2964(): pass

    label('loc_2964')

    OP_62(0x00F8, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)

    def _loc_2976(): pass

    label('loc_2976')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2998',
    )

    OP_62(0x00F9, 0x00000000, 2300, 0x28, 0x2B, 0x00000064, 0x03)

    Jump('loc_29CC')

    def _loc_2998(): pass

    label('loc_2998')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_29BA',
    )

    OP_62(0x00F9, 0x00000000, 1700, 0x28, 0x2B, 0x00000064, 0x03)

    Jump('loc_29CC')

    def _loc_29BA(): pass

    label('loc_29BA')

    OP_62(0x00F9, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)

    def _loc_29CC(): pass

    label('loc_29CC')

    CreateThread(0x00F8, 0x00, 0x00, func_0B_2CF1)
    CreateThread(0x00F9, 0x00, 0x00, func_0C_2D1D)
    WaitForThreadExit(0x00F8, 0x0000)
    WaitForThreadExit(0x00F9, 0x0000)

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2A4C',
    )

    OP_62(0x0108, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrSetDirection(0x0108, 0, 500)
    ChrMoveToRelative(0x0108, 0, 0, 1500, 3000, 0x00)

    ChrTalk(
        0x0108,
        (
            '#0080321447V#076F#6P这里！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2BF7')

    def _loc_2A4C(): pass

    label('loc_2A4C')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2AB8',
    )

    OP_62(0x0104, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrSetDirection(0x0104, 0, 500)
    ChrMoveToRelative(0x0104, 0, 0, 1500, 3000, 0x00)

    ChrTalk(
        0x0104,
        (
            '#0040321448V#530F#6P这里……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2BF7')

    def _loc_2AB8(): pass

    label('loc_2AB8')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2B20',
    )

    OP_62(0x0106, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrSetDirection(0x0106, 0, 500)
    ChrMoveToRelative(0x0106, 0, 0, 1500, 3000, 0x00)

    ChrTalk(
        0x0106,
        (
            '#0050321449V#054F#6P这里！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2BF7')

    def _loc_2B20(): pass

    label('loc_2B20')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2B8C',
    )

    OP_62(0x0103, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrSetDirection(0x0103, 0, 500)
    ChrMoveToRelative(0x0103, 0, 0, 1500, 3000, 0x00)

    ChrTalk(
        0x0103,
        (
            '#0030321450V#024F#6P这里……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2BF7')

    def _loc_2B8C(): pass

    label('loc_2B8C')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2BF7',
    )

    OP_62(0x0105, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrSetDirection(0x0105, 0, 500)
    ChrMoveToRelative(0x0105, 0, 0, 1500, 3000, 0x00)

    ChrTalk(
        0x0105,
        (
            '#0060321451V#046F#6P是这里……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2BF7(): pass

    label('loc_2BF7')

    @scena.Lambda('lambda_2BFD')
    def lambda_2BFD():
        CameraMove(-33100, 0, 90600, 3000)

        ExitThread()

    DispatchAsync(0x0109, 0x0001, lambda_2BFD)

    @scena.Lambda('lambda_2C15')
    def lambda_2C15():
        ChrSetDirection(0x00FE, 0, 500)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_2C15)

    Sleep(50)

    @scena.Lambda('lambda_2C28')
    def lambda_2C28():
        ChrSetDirection(0x00FE, 0, 500)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_2C28)

    Sleep(50)

    ChrSetDirection(0x0109, 0, 500)
    WaitForThreadExit(0x0109, 0x0001)
    Sleep(500)

    ChrTalk(
        0x0109,
        (
            '#0180321452V#1063F！！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0381, 7, 0x1C0F))
    Sleep(100)

    Fade(500)
    FormationDelMember(0x00, 0xFF)
    ChrSetPos(0x0000, -29120, 0, 69960, 0)
    ChrSetPos(0x0001, -29120, 0, 69960, 0)
    ChrSetPos(0x0002, -29120, 0, 69960, 0)
    OP_69(0x0000, 0)
    OP_6A(0x0000)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_0D()
    OP_D6(0x00)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x51),
            Expr.Nop,
            Expr.Return,
        ),
    )

    EventEnd(0x00)
    MapSetFlags(0x02000000)

    Return()

# id: 0x000B offset: 0x2CF1
@scena.Code('func_0B_2CF1')
def func_0B_2CF1():
    ChrSetDirection(0x00FE, 45, 400)
    Sleep(500)

    ChrSetDirection(0x00FE, 90, 400)
    Sleep(500)

    ChrSetDirection(0x00FE, 180, 400)
    Sleep(500)

    ChrSetDirection(0x00FE, 90, 400)

    Return()

# id: 0x000C offset: 0x2D1D
@scena.Code('func_0C_2D1D')
def func_0C_2D1D():
    ChrSetDirection(0x00FE, 0, 400)
    Sleep(500)

    ChrSetDirection(0x00FE, 270, 400)
    Sleep(500)

    ChrSetDirection(0x00FE, 45, 400)
    Sleep(500)

    ChrSetDirection(0x00FE, 270, 400)

    Return()

# id: 0x000D offset: 0x2D49
@scena.Code('func_0D_2D49')
def func_0D_2D49():
    EventBegin(0x01)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2D88',
    )

    ChrTalk(
        0x0109,
        (
            '#0180321460V#1063F（糟糕……不是这边！）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2EE3')

    def _loc_2D88(): pass

    label('loc_2D88')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2DC2',
    )

    ChrTalk(
        0x0107,
        (
            '#0070321461V#065F（不、不是这边啦！）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2EE3')

    def _loc_2DC2(): pass

    label('loc_2DC2')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2DFE',
    )

    ChrTalk(
        0x0105,
        (
            '#0060321462V#042F（不行……不是这边！）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2EE3')

    def _loc_2DFE(): pass

    label('loc_2DFE')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2E38',
    )

    ChrTalk(
        0x0103,
        (
            '#0030321463V#022F（不……不是这边！）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2EE3')

    def _loc_2E38(): pass

    label('loc_2E38')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2E74',
    )

    ChrTalk(
        0x0106,
        (
            '#0050321464V#057F（不行……不是这边！）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2EE3')

    def _loc_2E74(): pass

    label('loc_2E74')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2EAE',
    )

    ChrTalk(
        0x0104,
        (
            '#0040321465V#032F（不对……是对面！）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2EE3')

    def _loc_2EAE(): pass

    label('loc_2EAE')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2EE3',
    )

    ChrTalk(
        0x0108,
        (
            '#0080321466V#072F（不……是对面！）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2EE3(): pass

    label('loc_2EE3')

    ChrMoveToRelative(0x0000, 0, 0, 1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)
    MapSetFlags(0x02000000)

    Return()

# id: 0x000E offset: 0x2F04
@scena.Code('func_0E_2F04')
def func_0E_2F04():
    FadeOut(0, 0, -1)
    ClearScenaFlags(ScenaFlag(0x0240, 0, 0x1200))
    ClearScenaFlags(ScenaFlag(0x0240, 1, 0x1201))
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x05, 0xFF)
    FormationDelMember(0x09, 0xFF)

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
        (0x00000000, 'loc_2F81'),
        (0x00000001, 'loc_2F87'),
        (-1, 'loc_2F8D'),
    )

    def _loc_2F81(): pass

    label('loc_2F81')

    SetScenaFlags(ScenaFlag(0x0240, 0, 0x1200))

    Jump('loc_2F8D')

    def _loc_2F87(): pass

    label('loc_2F87')

    SetScenaFlags(ScenaFlag(0x0240, 1, 0x1201))

    Jump('loc_2F8D')

    def _loc_2F8D(): pass

    label('loc_2F8D')

    Return()

# id: 0x000F offset: 0x2F8E
@scena.Code('func_0F_2F8E')
def func_0F_2F8E():
    MapClearFlags(0x00000001)
    CameraMove(64510, 0, -14780, 92)
    Sleep(100)

    FadeIn(0, 0)

    OP_C9(
        0x00,
        (
            ChrTable['艾丝蒂尔'],
            ChrTable['凯文神父'],
            0x00FF,
            0x00FF,
        ),
        (
            ChrTable['阿加特'],
            ChrTable['雪拉扎德'],
            ChrTable['提妲'],
            ChrTable['奥利维尔'],
            ChrTable['科洛丝'],
            ChrTable['金'],
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

    FadeOut(0, 0, -1)
    OP_69(0x0000, 0)
    Sleep(1000)

    Return()

# id: 0x0010 offset: 0x2FEB
@scena.Code('func_10_2FEB')
def func_10_2FEB():
    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_303C',
    )

    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '导力好像停止了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    TalkEnd(0x00FF)

    Jump('loc_31F7')

    def _loc_303C(): pass

    label('loc_303C')

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '这是一台可供旅行者回复体力的导力器装置。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

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
        32,
        1,
        (
            TXT(0x00, '在这里休息\n'),
            TXT(0x01, '离开\n'),
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

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_31DC',
    )

    FadeIn(100, 0)
    Sleep(500)

    OP_26(13)
    StopEffect(0x00, 0x02)
    PlayEffect(0x00, 0x00, 0x00FF, -33630, 1000, 11690, 0, 0, 0, 700, 700, 700, 0x00FF, 0, 0, 0, 0)
    OP_6F(0x0000, 0)
    OP_70(0x0000, 50)
    OP_73(0x0000)
    OP_20(0x00000BB8)
    PlaySE(12, 0x00, 0x64)
    StopEffect(0x00, 0x02)
    LoadEffect(0x01, 'map\\\\mp027_01.eff')
    PlayEffect(0x01, 0x01, 0x00FF, -33630, 1000, 11690, 0, 0, 0, 1500, 1500, 1500, 0x00FF, 0, 0, 0, 0)
    FadeOut(1000, 0, -1)
    Sleep(700)

    PlaySE(13, 0x00, 0x64)
    OP_0D()
    ChrSetStatus(0x00FF, 0xFE, 0)
    OP_69(0x0000, 0)
    OP_30(0x01)
    Sleep(3500)

    StopEffect(0x01, 0x02)
    PlayEffect(0x00, 0x00, 0x00FF, -33630, 1000, 11690, 0, 0, 0, 1300, 1300, 1300, 0x00FF, 0, 0, 0, 0)
    OP_6F(0x0000, 0)
    OP_1E()
    FadeIn(1000, 0)
    OP_56(0x00)
    TalkEnd(0x00FF)

    Return()

    def _loc_31DC(): pass

    label('loc_31DC')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_31F6',
    )

    FadeIn(300, 0)
    TalkEnd(0x00FF)

    Return()

    def _loc_31F6(): pass

    label('loc_31F6')

    Return()

    def _loc_31F7(): pass

    label('loc_31F7')

    Return()

# id: 0x0011 offset: 0x31F8
@scena.Code('func_11_31F8')
def func_11_31F8():
    ClearScenaFlags(ScenaFlag(0x0393, 2, 0x1C9A))
    ClearScenaFlags(ScenaFlag(0x0393, 3, 0x1C9B))
    ClearScenaFlags(ScenaFlag(0x0393, 4, 0x1C9C))
    ClearScenaFlags(ScenaFlag(0x0393, 5, 0x1C9D))
    ClearScenaFlags(ScenaFlag(0x0393, 6, 0x1C9E))
    SetScenaFlags(ScenaFlag(0x0393, 7, 0x1C9F))

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
