import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import R1101_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('R1101   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '修理员'),
    TXT(0x02, '运输车'),
    TXT(0x03, '库拉茨'),
    TXT(0x04, '威尔特桥·关所方向'),
    TXT(0x05, '柏斯方向'),
    TXT(0x06, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Bose'
    header.mapModel       = 'R1101.x'
    header.mapIndex       = 55
    header.bgm            = 20
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x9EB
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
            word_3A         = 55,
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
        ('ED6_DT06/CH20078._CH', 'ED6_DT06/CH20078P._CP'),
        ('ED6_DT07/CH01260._CH', 'ED6_DT07/CH01260P._CP'),
        ('ED6_DT09/CH10290._CH', 'ED6_DT09/CH10290P._CP'),
        ('ED6_DT09/CH10291._CH', 'ED6_DT09/CH10291P._CP'),
        ('ED6_DT09/CH10320._CH', 'ED6_DT09/CH10320P._CP'),
        ('ED6_DT09/CH10321._CH', 'ED6_DT09/CH10321P._CP'),
        ('ED6_DT09/CH10350._CH', 'ED6_DT09/CH10350P._CP'),
        ('ED6_DT09/CH10351._CH', 'ED6_DT09/CH10351P._CP'),
        ('ED6_DT09/CH10870._CH', 'ED6_DT09/CH10870P._CP'),
        ('ED6_DT09/CH10871._CH', 'ED6_DT09/CH10871P._CP'),
    ]

# id: 0x10002 offset: 0xFA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = -64160,
            z                   = 0,
            y                   = 28100,
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
            x                   = -64160,
            z                   = 0,
            y                   = 28100,
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
            x                   = -65150,
            z                   = 0,
            y                   = 26800,
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
            x                   = -10250,
            z                   = 0,
            y                   = -8450,
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
            x                   = -106260,
            z                   = 0,
            y                   = -32340,
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

# id: 0x10003 offset: 0x19A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            x           = -46450,
            z           = 30,
            y           = 2310,
            word_0C     = 0x0000,
            word_0E     = 0x0006,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x00E6,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -72920,
            z           = -30,
            y           = 51450,
            word_0C     = 0x0000,
            word_0E     = 0x0006,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x00E6,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -97850,
            z           = -30,
            y           = 45380,
            word_0C     = 0x0000,
            word_0E     = 0x0006,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x00E3,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -90070,
            z           = 1040,
            y           = 27970,
            word_0C     = 0x0000,
            word_0E     = 0x0004,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x00E7,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -114180,
            z           = 80,
            y           = -40,
            word_0C     = 0x0000,
            word_0E     = 0x0004,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x00E7,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10004 offset: 0x226
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = -71266,
            y           = -2000,
            z           = 12121,
            range       = -55060,
            dword_10    = 0x000007D0,
            dword_14    = 0x00003E8F,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000003,
        ),
    )

# id: 0x10005 offset: 0x246
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x246
@scena.Code('PreInit')
def PreInit():
    Return()

# id: 0x0001 offset: 0x247
@scena.Code('Init')
def Init():
    OP_16(0x02, 4000, -203000, -113000, 196630)
    OP_71(0x0000, 0x0004)

    Return()

# id: 0x0002 offset: 0x25F
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_274',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('ReInit')

    def _loc_274(): pass

    label('loc_274')

    Return()

# id: 0x0003 offset: 0x275
@scena.Code('func_03_275')
def func_03_275():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0060, 5, 0x305)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_952',
    )

    SetScenaFlags(ScenaFlag(0x0060, 5, 0x305))
    OP_28(0x0007, 0x04, 0x40)
    OP_28(0x000C, 0x04, 0x40)

    If(
        (
            (Expr.Eval, "OP_40(0x0329)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_298',
    )

    OP_28(0x000D, 0x04, 0x40)

    def _loc_298(): pass

    label('loc_298')

    EventBegin(0x00)
    OP_62(0x0000, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    ChrTurnDirection(0x0000, 0x000A, 400)
    OP_62(0x0001, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    ChrTurnDirection(0x0001, 0x000A, 400)
    OP_62(0x0002, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    ChrTurnDirection(0x0002, 0x000A, 400)
    Sleep(500)

    @scena.Lambda('lambda_02FF')
    def lambda_02FF():
        ChrTurnDirection(0x00FE, 0x000A, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_02FF)

    @scena.Lambda('lambda_030D')
    def lambda_030D():
        ChrTurnDirection(0x00FE, 0x000A, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_030D)

    @scena.Lambda('lambda_031B')
    def lambda_031B():
        ChrTurnDirection(0x00FE, 0x000A, 400)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_031B)

    ChrTalk(
        0x0101,
        (
            '#0010020321V#004F那是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_72(0x0000, 0x0004)
    OP_71(0x0000, 0x0020)
    SetChrPos(0x0009, -64060, 0, 32450, 180)
    SetChrFlags(0x0009, 0x0004)
    SetChrFlags(0x0009, 0x0040)
    OP_A1(0x0009, 0x0000)
    OP_71(0x0000, 0x0040)
    SetChrPos(0x000A, -65360, 0, 30700, 180)
    PlaySE(207, 0x01, 0x64)
    CreateThread(0x0009, 0x02, 0x00, 0x0004)

    @scena.Lambda('lambda_038F')
    def lambda_038F():
        ChrMoveTo(0x00FE, -64180, 0, 19360, 1700, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_038F)

    @scena.Lambda('lambda_03AA')
    def lambda_03AA():
        ChrWalkTo(0x00FE, -65670, 0, 17910, 1700, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_03AA)

    LoadEffect(0x00, 'map\\\\mp024_00.eff')
    PlayEffect(0x00, 0x00, 0x0009, 0, 200, -7000, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0x01, 0x0009, 0, 200, -4000, 0, 0, 0, 1000, 500, 500, 0x00FF, 0, 0, 0, 0)
    SetChrFlags(0x0008, 0x0020)
    ClearChrFlags(0x0008, 0x0080)
    ClearChrFlags(0x000A, 0x0080)
    SetChrFlags(0x0008, 0x0040)
    SetChrFlags(0x0009, 0x0040)
    SetChrFlags(0x000A, 0x0040)

    @scena.Lambda('lambda_0461')
    def lambda_0461():
        OP_6C(335000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0461)

    Yield()
    SetChrBattleFlags(0x0008, 0x0020)
    OP_89(0x0008, -63900, 1600, 32000, 180)
    CameraMove(-63960, 0, 26270, 3000)
    SetChrPos(0x0101, -66870, 0, 15150, 358)
    SetChrPos(0x0102, -68360, 310, 16180, 55)
    SetChrPos(0x0103, -67000, 10, 16650, 326)

    @scena.Lambda('lambda_04CC')
    def lambda_04CC():
        ChrTurnDirection(0x00FE, 0x000A, 0)
        Yield()

        Jump('lambda_04CC')

    DispatchAsync2(0x0101, 0x0001, lambda_04CC)

    @scena.Lambda('lambda_04DD')
    def lambda_04DD():
        ChrTurnDirection(0x00FE, 0x000A, 0)
        Yield()

        Jump('lambda_04DD')

    DispatchAsync2(0x0102, 0x0001, lambda_04DD)

    @scena.Lambda('lambda_04EE')
    def lambda_04EE():
        ChrTurnDirection(0x00FE, 0x000A, 0)
        Yield()

        Jump('lambda_04EE')

    DispatchAsync2(0x0103, 0x0001, lambda_04EE)

    CameraMove(-65780, 0, 17980, 5000)
    WaitForThreadExit(0x0009, 0x0001)
    OP_24(0x00CF, 0x50)
    StopEffect(0x00, 0x02)
    StopEffect(0x01, 0x02)
    WaitForThreadExit(0x000A, 0x0001)

    ChrTalk(
        0x000A,
        (
            '#0310020322V#821F#4P哟！\n',
            '这不是雪拉扎德吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030020323V#023F库拉茨，好久不见了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030020324V你为什么会来这种地方啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0310020325V#820F#4P正如你所见，我在执行护卫工作。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0310020326V拜上次那个事件所赐，\n',
            '定期船停航的消息你也知道了吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0310020327V所以，囤积的货物\n',
            '就只能从陆路运往王都了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030020328V#020F原来如此，真是辛苦你了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0310020329V#820F#4P这么说来，\n',
            '你身边的那些年轻人是干什么的？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0310020330V难道说……\n',
            '你们打算调查那个事件？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030020331V#023F没错啊。\n',
            '……怎么了，有什么问题吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0310020332V#823F#4P算了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0310020333V#820F详细的情况，\n',
            '还是到柏斯支部去问卢格兰爷爷吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0310020334V那么，再见吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_076E')
    def lambda_076E():
        ChrWalkTo(0x00FE, -62120, 0, -39780, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_076E)

    Sleep(300)

    @scena.Lambda('lambda_078E')
    def lambda_078E():
        ChrMoveTo(0x00FE, -62120, 0, -39780, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_078E)

    OP_24(0x00CF, 0x64)
    PlayEffect(0x00, 0x00, 0x0009, 0, 200, -7000, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0x01, 0x0009, 0, 200, -4000, 0, 0, 0, 1000, 500, 500, 0x00FF, 0, 0, 0, 0)
    Sleep(1000)

    CameraMove(-67630, 60, 16050, 5000)
    CreateThread(0x0009, 0x02, 0x00, 0x0005)
    OP_62(0x0101, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(2000)

    OP_63(0x0101)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0103, 0xFF)

    ChrTalk(
        0x0101,
        (
            '#0010020335V#505F刚才阿斯顿队长也是……\n',
            '怎么大家说话时都支支吾吾的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020020336V#012F看样子是发生了什么事情。\n',
            '还是先到游击士协会看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030020337V#026F好了，正如他所说的，\n',
            '到柏斯支部就会明白了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030020338V#020F那么，快些赶路吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    StopEffect(0x00, 0x02)
    StopEffect(0x01, 0x02)
    SetChrFlags(0x0008, 0x0080)
    SetChrFlags(0x000A, 0x0080)
    OP_71(0x0000, 0x0004)
    EventEnd(0x00)

    def _loc_952(): pass

    label('loc_952')

    Return()

# id: 0x0004 offset: 0x953
@scena.Code('func_04_953')
def func_04_953():
    OP_24(0x00CF, 0x41)
    Sleep(100)

    OP_24(0x00CF, 0x46)
    Sleep(100)

    OP_24(0x00CF, 0x4B)
    Sleep(100)

    OP_24(0x00CF, 0x50)
    Sleep(100)

    OP_24(0x00CF, 0x55)
    Sleep(100)

    OP_24(0x00CF, 0x5A)
    Sleep(100)

    OP_24(0x00CF, 0x5F)
    Sleep(100)

    OP_24(0x00CF, 0x64)

    Return()

# id: 0x0005 offset: 0x997
@scena.Code('func_05_997')
def func_05_997():
    Sleep(1000)

    OP_24(0x00CF, 0x5F)
    Sleep(100)

    OP_24(0x00CF, 0x5A)
    Sleep(100)

    OP_24(0x00CF, 0x55)
    Sleep(100)

    OP_24(0x00CF, 0x50)
    Sleep(100)

    OP_24(0x00CF, 0x4B)
    Sleep(100)

    OP_24(0x00CF, 0x46)
    Sleep(100)

    OP_24(0x00CF, 0x41)
    Sleep(100)

    OP_23(0x00CF)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
