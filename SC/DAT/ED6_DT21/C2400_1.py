import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C2400_1_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C2400_1 ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Ruan'
    header.mapModel       = 'C2400.x'
    header.mapIndex       = 97
    header.bgm            = 125
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
    ]

# id: 0x10001 offset: 0xA8
@scena.NpcData('NpcData')
def NpcData():
    return (
    )

# id: 0x10002 offset: 0xA8
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0xA8
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0xA8
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0xA8
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_B9',
    )

    Call(1, 0x0015)

    def _loc_B9(): pass

    label('loc_B9')

    EventBegin(0x00)
    CameraMove(-170, 0, 490, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2600, 0)
    OP_6C(44000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, -10, 0, 5410, 1)
    ChrSetPos(0x00F7, -10, 0, 5410, 1)
    ChrSetPos(0x0105, -10, 0, 5410, 1)
    ChrSetPos(0x0104, -10, 0, 5410, 1)
    ChrSetPos(0x0127, -10, 0, 5410, 1)
    ChrClearFlags(0x0011, 0x0080)
    ChrSetFlags(0x0011, 0x0040)
    ChrSetPos(0x0011, -320, 0, -8670, 7)
    FadeOut(0, 0, -1)
    FadeIn(2000, 0)

    @scena.Lambda('lambda_0181')
    def lambda_0181():
        ChrWalkTo(0x0101, -170, 0, 490, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_0181)

    Sleep(500)

    @scena.Lambda('lambda_01A1')
    def lambda_01A1():
        ChrWalkTo(0x0105, -170, 0, 2600, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0105, 0x0000, lambda_01A1)

    Sleep(500)

    @scena.Lambda('lambda_01C1')
    def lambda_01C1():
        ChrWalkTo(0x00F7, -170, 0, 2600, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00F7, 0x0000, lambda_01C1)

    @scena.Lambda('lambda_01DC')
    def lambda_01DC():
        ChrWalkTo(0x0105, 760, 0, 700, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0105, 0x0000, lambda_01DC)

    Sleep(500)

    @scena.Lambda('lambda_01FC')
    def lambda_01FC():
        ChrWalkTo(0x0104, -170, 0, 2600, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0104, 0x0000, lambda_01FC)

    @scena.Lambda('lambda_0217')
    def lambda_0217():
        ChrWalkTo(0x00F7, -980, 0, 1560, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00F7, 0x0000, lambda_0217)

    Sleep(500)

    @scena.Lambda('lambda_0237')
    def lambda_0237():
        ChrWalkTo(0x0127, -100, 0, 3000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0127, 0x0000, lambda_0237)

    @scena.Lambda('lambda_0252')
    def lambda_0252():
        ChrWalkTo(0x0104, 370, 0, 1800, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0104, 0x0000, lambda_0252)

    WaitForThreadExit(0x0101, 0x0000)
    Sleep(500)

    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    @scena.Lambda('lambda_0293')
    def lambda_0293():
        CameraMove(0, 0, -3920, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_0293)

    @scena.Lambda('lambda_02AB')
    def lambda_02AB():
        OP_67(0, 7000, -10000, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_02AB)

    WaitForThreadExit(0x0101, 0x0000)
    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010211538V#1020F#4P咦……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_326',
    )

    ChrTalk(
        0x0106,
        (
            '#0050211539V#054F#7P切……这么快就来了吗！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_358')

    def _loc_326(): pass

    label('loc_326')

    ChrTalk(
        0x0103,
        (
            '#0030211540V#523F#7P可恶……这么快就来了吗！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_358(): pass

    label('loc_358')

    Fade(250)
    PlaySE(213, 0x00, 0x64)
    ChrSetChipByIndex(0x0101, 13)
    ChrSetSubChip(0x0101, 0)
    ChrSetChipByIndex(0x0105, 17)
    ChrSetSubChip(0x0105, 0)
    ChrSetChipByIndex(0x0104, 16)
    ChrSetSubChip(0x0104, 0)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_394',
    )

    ChrSetChipByIndex(0x0106, 15)
    ChrSetSubChip(0x0106, 0)

    Jump('loc_39E')

    def _loc_394(): pass

    label('loc_394')

    ChrSetChipByIndex(0x0103, 14)
    ChrSetSubChip(0x0103, 0)

    def _loc_39E(): pass

    label('loc_39E')

    OP_62(0x0127, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    OP_0D()
    TerminateThread(0x0011, 0xFF)
    ChrSetFlags(0x0011, 0x0020)
    ChrSetChipByIndex(0x0011, 30)
    ChrSetSubChip(0x0011, 0)

    @scena.Lambda('lambda_03CA')
    def lambda_03CA():
        OP_99(0x00FE, 0x00, 0x01, 2000)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_03CA)

    Sleep(500)

    @scena.Lambda('lambda_03DF')
    def lambda_03DF():
        OP_99(0x00FE, 0x01, 0x05, 5000)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_03DF)

    @scena.Lambda('lambda_03EF')
    def lambda_03EF():
        ChrMoveTo(0x00FE, 10, 0, -2100, 15000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0000, lambda_03EF)

    @scena.Lambda('lambda_040A')
    def lambda_040A():
        CameraMove(100, 0, -930, 500)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_040A)

    @scena.Lambda('lambda_0422')
    def lambda_0422():
        OP_67(0, 6000, -10000, 500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0422)

    Sleep(500)

    TerminateThread(0x0011, 0x00)
    TerminateThread(0x0011, 0x01)
    TerminateThread(0x0101, 0x00)
    TerminateThread(0x0101, 0x01)
    Battle(0x00000398, 0x00000000, 0x00, 0x0000, 0xFF)
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    Sleep(500)

    ChrSetPos(0x0101, -170, 0, 490, 180)
    ChrSetPos(0x0105, 760, 0, 700, 180)
    ChrSetPos(0x00F7, -980, 0, 1560, 180)
    ChrSetPos(0x0127, -100, 0, 3000, 180)
    ChrSetPos(0x0104, 370, 0, 1800, 180)
    ChrSetFlags(0x0011, 0x0080)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)

    ExecExpressionWithVar(
        0x65,
        (
            (Expr.GetChrWork, 0x101, 0x1),
            (Expr.GetChrWork, 0x127, 0x1),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x66,
        (
            (Expr.GetChrWork, 0x101, 0x2),
            (Expr.GetChrWork, 0x127, 0x2),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x67,
        (
            (Expr.GetChrWork, 0x101, 0x3),
            (Expr.GetChrWork, 0x127, 0x3),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010211541V#1007F还、还真厉害呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010211542V#1002F不过……\n',
            '这里是地下遗迹？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060211543V#042F是啊……\n',
            '看来这是中世纪的地下建筑。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060211544V想不到还有这种地方……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040211545V#030F#5P呼，魔兽的气息\n',
            '弥漫在四周呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040211546V#035F总之，这地下遗迹\n',
            '就是卡片上所写的『试炼』吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(500)
    ChrSetChipByIndex(0x0101, 65535)
    ChrSetSubChip(0x0101, 0)
    ChrSetChipByIndex(0x0105, 65535)
    ChrSetSubChip(0x0105, 0)
    ChrSetChipByIndex(0x0104, 65535)
    ChrSetSubChip(0x0104, 0)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_691',
    )

    ChrSetChipByIndex(0x0106, 65535)
    ChrSetSubChip(0x0106, 0)

    Jump('loc_69B')

    def _loc_691(): pass

    label('loc_691')

    ChrSetChipByIndex(0x0103, 65535)
    ChrSetSubChip(0x0103, 0)

    def _loc_69B(): pass

    label('loc_69B')

    OP_0D()
    Sleep(500)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_802',
    )

    ChrTalk(
        0x0106,
        (
            '#0050211547V#053F#6P带非战斗人员进去这种地方\n',
            '毕竟还是很不妥的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_06F3')
    def lambda_06F3():
        ChrTurnDirection(0x00FE, 0x0127, 400)
        Yield()

        Jump('lambda_06F3')

    DispatchAsync2(0x00F7, 0x0001, lambda_06F3)

    Sleep(400)

    ChrTalk(
        0x0106,
        (
            '#0050211548V#050F#6P喂，摄影师小姐。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0733')
    def lambda_0733():
        ChrTurnDirection(0x00FE, 0x0127, 400)
        Yield()

        Jump('lambda_0733')

    DispatchAsync2(0x0101, 0x0001, lambda_0733)

    Sleep(100)

    @scena.Lambda('lambda_0749')
    def lambda_0749():
        ChrTurnDirection(0x00FE, 0x0127, 400)
        Yield()

        Jump('lambda_0749')

    DispatchAsync2(0x0105, 0x0001, lambda_0749)

    Sleep(100)

    @scena.Lambda('lambda_075F')
    def lambda_075F():
        ChrTurnDirection(0x00FE, 0x0127, 400)
        Yield()

        Jump('lambda_075F')

    DispatchAsync2(0x0104, 0x0001, lambda_075F)

    Sleep(100)

    ChrTurnDirection(0x0127, 0x00F7, 400)

    ChrTalk(
        0x0127,
        (
            '#0280211549V#153F嗯，什么事～？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050211550V#050F#6P你也听到了，\n',
            '前面会相当危险。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050211551V你就先在前面那个\n',
            '房间里待命吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_95D')

    def _loc_802(): pass

    label('loc_802')

    ChrTalk(
        0x0103,
        (
            '#0030211552V#026F#6P带非战斗人员进去这种地方\n',
            '毕竟还是很危险呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_084F')
    def lambda_084F():
        ChrTurnDirection(0x00FE, 0x0127, 400)
        Yield()

        Jump('lambda_084F')

    DispatchAsync2(0x00F7, 0x0001, lambda_084F)

    Sleep(400)

    ChrTalk(
        0x0103,
        (
            '#0030211553V#020F#6P我说，朵洛希小姐。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0891')
    def lambda_0891():
        ChrTurnDirection(0x00FE, 0x0127, 400)
        Yield()

        Jump('lambda_0891')

    DispatchAsync2(0x0101, 0x0001, lambda_0891)

    Sleep(100)

    @scena.Lambda('lambda_08A7')
    def lambda_08A7():
        ChrTurnDirection(0x00FE, 0x0127, 400)
        Yield()

        Jump('lambda_08A7')

    DispatchAsync2(0x0105, 0x0001, lambda_08A7)

    Sleep(100)

    @scena.Lambda('lambda_08BD')
    def lambda_08BD():
        ChrTurnDirection(0x00FE, 0x0127, 400)
        Yield()

        Jump('lambda_08BD')

    DispatchAsync2(0x0104, 0x0001, lambda_08BD)

    Sleep(100)

    ChrTurnDirection(0x0127, 0x00F7, 400)

    ChrTalk(
        0x0127,
        (
            '#0280211549V#153F嗯，什么事～？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030211555V#020F#6P你也听到了，\n',
            '前面会相当危险。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030211556V你就先在前面那个\n',
            '房间里待命吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_95D(): pass

    label('loc_95D')

    ChrTalk(
        0x0127,
        (
            '#0280211557V#154F啊～怎么这样啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280211558V好不容易才有\n',
            '拍摄幽灵的机会～……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010211559V#1006F好啦，我们发现什么的话\n',
            '会回来叫你的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010211560V这样就没问题了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0127, 0x0101, 400)

    ChrTalk(
        0x0127,
        (
            '#0280211561V#154F唔～没办法。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280211562V那么大家\n',
            '要小心啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0127, 0, 400)
    ChrWalkTo(0x0127, 0, 0, 5410, 2000, 0x00)
    ChrSetRGBAMask(0x0127, 255, 255, 255, 0, 400)
    ChrSetFlags(0x0004, 0x0008)
    FormationDelMember(0x26, 0xFF)
    TerminateThread(0x0101, 0x01)
    TerminateThread(0x00F7, 0x01)
    TerminateThread(0x0105, 0x01)
    TerminateThread(0x0104, 0x01)
    ChrSetDirection(0x00F7, 180, 400)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_B0A',
    )

    ChrTalk(
        0x0106,
        (
            '#0050211563V#051F#1P那么……\n',
            '我们前进吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050211564V魔兽也相当不好对付。\n',
            '要慎重地前进。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B6A')

    def _loc_B0A(): pass

    label('loc_B0A')

    ChrTalk(
        0x0103,
        (
            '#0030211565V#022F#1P那么……\n',
            '我们前进吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030211566V魔兽也相当不好对付。\n',
            '要慎重地前进。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_B6A(): pass

    label('loc_B6A')

    @scena.Lambda('lambda_0B70')
    def lambda_0B70():
        ChrTurnDirection(0x00FE, 0x00F7, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0B70)

    @scena.Lambda('lambda_0B7E')
    def lambda_0B7E():
        ChrTurnDirection(0x00FE, 0x00F7, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_0B7E)

    @scena.Lambda('lambda_0B8C')
    def lambda_0B8C():
        ChrTurnDirection(0x00FE, 0x00F7, 400)

        ExitThread()

    DispatchAsync(0x0104, 0x0001, lambda_0B8C)

    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010211567V#1005F明白！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060211568V#042F明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040211569V#031F#5P呵呵，交给我吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0245, 2, 0x122A))
    EventEnd(0x00)

    Return()

# id: 0x0001 offset: 0xC06
@scena.Code('func_01_C06')
def func_01_C06():
    Call(1, 0x0002)
    Call(1, 0x0003)

    Return()

# id: 0x0002 offset: 0xC0F
@scena.Code('func_02_C0F')
def func_02_C0F():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_C20',
    )

    Call(1, 0x0015)

    def _loc_C20(): pass

    label('loc_C20')

    EventBegin(0x00)
    FadeOut(0, 0, -1)
    MapClearFlags(0x00000001)
    ChrClearFlags(0x000F, 0x0080)
    ChrSetFlags(0x000F, 0x0040)
    ChrSetFlags(0x000F, 0x0004)
    ChrSetFlags(0x000F, 0x0001)
    ChrSetPos(0x0101, -262000, 0, 74000, 360)
    ChrSetPos(0x0105, -263500, 0, 73700, 360)
    ChrSetPos(0x00F7, -262000, 0, 72550, 360)
    ChrSetPos(0x0104, -264000, 0, 72550, 360)
    ChrSetPos(0x000F, -263000, 150, 90390, 9)
    CameraMove(-262870, 0, 73230, 0)
    OP_67(0, 6280, -10000, 0)
    CameraSetDistance(1500, 0)
    OP_6C(45000, 0)
    OP_6E(513, 0)
    OP_20(0x000007D0)
    FadeIn(1000, 0)
    OP_0D()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010211572V#1004F啊……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlayBGM(111)

    @scena.Lambda('lambda_0D2A')
    def lambda_0D2A():
        CameraMove(-262290, 0, 87050, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_0D2A)

    @scena.Lambda('lambda_0D42')
    def lambda_0D42():
        OP_67(0, 6810, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0D42)

    @scena.Lambda('lambda_0D5A')
    def lambda_0D5A():
        CameraSetDistance(1810, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0D5A)

    WaitForThreadExit(0x0101, 0x0000)
    WaitForThreadExit(0x0101, 0x0002)
    ChrSetPos(0x0101, -262000, 0, 75500, 360)
    ChrSetPos(0x0105, -264000, 0, 75500, 360)
    ChrSetPos(0x00F7, -262000, 0, 74500, 360)
    ChrSetPos(0x0104, -264000, 0, 74500, 360)

    @scena.Lambda('lambda_0DB8')
    def lambda_0DB8():
        ChrWalkTo(0x00FE, -262500, 0, 84500, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0DB8)

    Sleep(300)

    @scena.Lambda('lambda_0DD8')
    def lambda_0DD8():
        ChrWalkTo(0x00FE, -264000, 0, 84000, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_0DD8)

    Sleep(150)

    @scena.Lambda('lambda_0DF8')
    def lambda_0DF8():
        ChrWalkTo(0x00FE, -262000, 0, 83000, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_0DF8)

    Sleep(300)

    @scena.Lambda('lambda_0E18')
    def lambda_0E18():
        ChrWalkTo(0x00FE, -264000, 0, 82600, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0104, 0x0001, lambda_0E18)

    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x0105, 0x0001)
    WaitForThreadExit(0x00F7, 0x0001)
    WaitForThreadExit(0x0104, 0x0001)
    Sleep(500)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_EB7',
    )

    ChrTalk(
        0x0106,
        (
            '#0050211573V#057F#2P好像有影子，\n',
            '不过，看上去不像是幽灵……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050211574V你这家伙……是什么人！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F16')

    def _loc_EB7(): pass

    label('loc_EB7')

    ChrTalk(
        0x0103,
        (
            '#0030211575V#022F#2P好像有影子，\n',
            '不过，看上去不像是幽灵……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030211576V你到底是什么人？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_F16(): pass

    label('loc_F16')

    NpcTalk(
        0x000F,
        '神秘男子',
        (
            '#0170211577V#5P呵呵呵……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x000F, 180, 400)

    NpcTalk(
        0x000F,
        '戴面具的男人',
        (
            '#0170211578V#230F欢迎来到我的临时居所。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0170211579V来接受我的款待吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010211580V#1020F#2P面、面具……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060211581V#042F#2P与艾丝蒂尔和波利的\n',
            '目击情报一模一样呢……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060211582V你就是在卢安各地引起骚动的\n',
            '『影子』的真面目吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x000F,
        '戴面具的男人',
        (
            '#0170211583V#231F呵呵……\n',
            '确实如此，科洛蒂娅公主。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0170211584V很荣幸见到您。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0105, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010211585V#1005F#2P这、这家伙……\n',
            '为什么知道科洛丝的真实身份！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x000F,
        '戴面具的男人',
        (
            '#0170211586V#231F呵呵……\n',
            '世上没有我偷不到的秘密。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0170211587V郑重自我介绍一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_C5(0x00, 0, 0, 640, 512, 75, 0, 768, 512, 0, 0, 640, 512, 0x00FFFFFF, 0x00, 'C_VIS114._CH')
    OP_C6(0x00, 0x00, 100000, 0, 500)
    OP_C6(0x00, 0x03, -1, 500, 0)
    Sleep(1000)

    SetMessageWindowPos(72, 320, 56, 3)
    TalkSetChrName('戴面具的男人')

    Talk(
        (
            '#0170211588V#230F执行者ＮＯ．Ⅹ。\n',
            '『怪盗绅士』布卢布兰──',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0170211589V『噬身之蛇』的一员。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_C6(0x00, 0x03, 16777215, 250, 0)
    Sleep(250)

    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0104, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x00F7, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0105, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(500)

    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010211590V#1020F#2P噬身之蛇！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_1310',
    )

    ChrTalk(
        0x0106,
        (
            '#0050211591V#057F#2P……切……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1336')

    def _loc_1310(): pass

    label('loc_1310')

    ChrTalk(
        0x0103,
        (
            '#0030211592V#523F#2P……唔……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1336(): pass

    label('loc_1336')

    @scena.Lambda('lambda_133C')
    def lambda_133C():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, -400, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_133C)

    Sleep(50)

    @scena.Lambda('lambda_135C')
    def lambda_135C():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, -400, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_135C)

    Sleep(50)

    @scena.Lambda('lambda_137C')
    def lambda_137C():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, -400, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_137C)

    Sleep(50)

    @scena.Lambda('lambda_139C')
    def lambda_139C():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, -400, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0104, 0x0001, lambda_139C)

    WaitForThreadExit(0x0104, 0x0001)
    Sleep(500)

    ChrTalk(
        0x000F,
        (
            '#0170211593V#231F呵呵……\n',
            '不用那么杀气腾腾的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0170211594V我只是在这里做一个\n',
            '小小的实验而已。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0170211595V完全没有和诸位争斗的意思。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010211596V#1002F#2P实、实验……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1477')
    def lambda_1477():
        CameraMove(-262290, 0, 88050, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_1477)

    WaitForThreadExit(0x0101, 0x0000)
    WaitForThreadExit(0x0101, 0x0001)
    LoadEffect(0x00, 'map\\\\mp044_00.eff')
    PlayEffect(0x00, 0x00, 0x00FF, -263200, 1250, 92150, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlaySE(128, 0x00, 0x64)
    WaitEffect(0x00, 0x02)
    Sleep(1000)

    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010211597V#1020F#2P那、那是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060211598V#042F#2P理查德上校使用过的\n',
            '漆黑色的导力器『福音』……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040211599V#032F#2P而且……\n',
            '看来比那个还要大一圈。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0170211600V#230F呵呵，和他的报告一样，\n',
            '你们知道有这东西存在啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0170211601V这个『福音』\n',
            '是为了实验而开发的新型号。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0170211602V在这次的实验中\n',
            '起了很大的作用呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_1693',
    )

    ChrTalk(
        0x0106,
        (
            '#0050211603V#057F#2P实验……\n',
            '到底是什么实验？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_16C6')

    def _loc_1693(): pass

    label('loc_1693')

    ChrTalk(
        0x0103,
        (
            '#0030211604V#022F#2P实验……\n',
            '到底是什么实验？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_16C6(): pass

    label('loc_16C6')

    ChrTalk(
        0x000F,
        (
            '#0170211605V#231F呵呵呵……\n',
            '百闻不如一见。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0170211606V请你们亲眼看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x000F, 225, 400)
    ChrMoveTo(0x000F, -262300, 150, 91670, 2000, 0x00)
    ChrSetDirection(0x000F, 264, 400)
    Sleep(500)

    PlaySE(156, 0x00, 0x64)
    Sleep(500)

    Sleep(500)

    PlaySE(157, 0x00, 0x64)
    LoadEffect(0x01, 'map\\\\mp088_00.eff')
    PlayEffect(0x01, 0x00, 0x00FF, -263120, 80, 93290, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Fade(500)
    ChrClearFlags(0x0010, 0x0001)
    ChrSetRGBAMask(0x0010, 255, 255, 255, 170, 0)
    ChrClearFlags(0x0010, 0x0080)
    ChrSetPos(0x0010, -263000, 500, 89640, 180)
    CreateThread(0x0010, 0x01, 0x01, 0x000C)
    OP_0D()
    Sleep(500)

    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0104, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x00F7, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0105, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010211607V#1020F#2P幽、幽灵……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040211608V#030F不是幽灵，是使用了导力装置\n',
            '投射到空间之中的影像。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040211609V我从未听说过这种技术已经被实现了，\n',
            '看来是我孤陋寡闻了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x000F, 180, 400)

    ChrTalk(
        0x000F,
        (
            '#0170211610V#230F这是用我们的技术\n',
            '制造出来的空间投影装置。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0170211611V原本靠单一装置的能力\n',
            '只能实现把影像投射到眼前的距离……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0170211612V不过加上了『福音』的力量之后，\n',
            '像这样的事情也可以办到了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    LoadEffect(0x00, 'map\\\\mp045_00.eff')
    PlaySE(144, 0x00, 0x64)
    PlayEffect(0x00, 0x01, 0x00FF, -263200, 850, 92150, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(1000)

    @scena.Lambda('lambda_1A1A')
    def lambda_1A1A():
        CameraMove(-262290, 0, 85000, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_1A1A)

    @scena.Lambda('lambda_1A32')
    def lambda_1A32():
        OP_67(0, 6280, -10000, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1A32)

    Sleep(900)

    Fade(500)
    ChrClearFlags(0x0010, 0x0080)
    ChrSetFlags(0x0010, 0x0004)
    ChrSetFlags(0x0010, 0x0040)
    ChrSetPos(0x0010, -263000, 500, 80000, 360)
    OP_0D()
    WaitForThreadExit(0x0101, 0x0000)
    WaitForThreadExit(0x0101, 0x0001)
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0105, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x00F7, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0104, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(300)

    @scena.Lambda('lambda_1AE5')
    def lambda_1AE5():
        ChrTurnDirection(0x00FE, 0x0010, 600)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1AE5)

    @scena.Lambda('lambda_1AF3')
    def lambda_1AF3():
        ChrTurnDirection(0x00FE, 0x0010, 600)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_1AF3)

    @scena.Lambda('lambda_1B01')
    def lambda_1B01():
        ChrTurnDirection(0x00FE, 0x0010, 600)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_1B01)

    @scena.Lambda('lambda_1B0F')
    def lambda_1B0F():
        ChrTurnDirection(0x00FE, 0x0010, 600)

        ExitThread()

    DispatchAsync(0x0104, 0x0001, lambda_1B0F)

    Sleep(600)

    ChrTalk(
        0x0105,
        (
            '#0060211613V#044F#1P呀……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010211614V#1020F#5P哇哇……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1B69')
    def lambda_1B69():
        ChrTurnDirection(0x00FE, 0x0010, 0)
        Yield()

        Jump('lambda_1B69')

    DispatchAsync2(0x0101, 0x0001, lambda_1B69)

    @scena.Lambda('lambda_1B7A')
    def lambda_1B7A():
        ChrTurnDirection(0x00FE, 0x0010, 0)
        Yield()

        Jump('lambda_1B7A')

    DispatchAsync2(0x00F7, 0x0001, lambda_1B7A)

    @scena.Lambda('lambda_1B8B')
    def lambda_1B8B():
        ChrTurnDirection(0x00FE, 0x0010, 0)
        Yield()

        Jump('lambda_1B8B')

    DispatchAsync2(0x0105, 0x0001, lambda_1B8B)

    @scena.Lambda('lambda_1B9C')
    def lambda_1B9C():
        ChrTurnDirection(0x00FE, 0x0010, 0)
        Yield()

        Jump('lambda_1B9C')

    DispatchAsync2(0x0104, 0x0001, lambda_1B9C)

    ChrSetChipByIndex(0x0010, 22)
    ChrSetSubChip(0x0010, 0)
    CreateThread(0x0010, 0x01, 0x01, 0x000C)
    OP_97(0x0010, -262880, 83120, -600000, 7000, 0x0001)
    OP_97(0x0010, -262880, 83120, -230000, 5000, 0x0001)
    ChrTurnDirection(0x0010, 0x000F, 0)
    ChrMoveTo(0x0010, -263000, 150, 89640, 2000, 0x00)
    TerminateThread(0x0101, 0x01)
    TerminateThread(0x00F7, 0x01)
    TerminateThread(0x0105, 0x01)
    TerminateThread(0x0104, 0x01)
    ChrSetChipByIndex(0x0010, 23)
    ChrSetSubChip(0x0010, 0)
    ChrSetDirection(0x0010, 180, 400)
    Sleep(500)

    PlaySE(156, 0x00, 0x64)
    Sleep(500)

    StopEffect(0x00, 0x02)
    StopEffect(0x01, 0x02)
    OP_23(0x0090)
    Sleep(1000)

    Fade(1000)
    ChrSetFlags(0x0010, 0x0080)
    TerminateThread(0x000F, 0x01)
    TerminateThread(0x0010, 0x01)
    TerminateThread(0x0010, 0x03)
    ChrSetSubChip(0x000F, 0)
    OP_0D()
    Sleep(500)

    @scena.Lambda('lambda_1C62')
    def lambda_1C62():
        CameraMove(-262290, 0, 87050, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_1C62)

    @scena.Lambda('lambda_1C7A')
    def lambda_1C7A():
        OP_67(0, 6810, -10000, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1C7A)

    ChrWalkTo(0x000F, -263000, 150, 90390, 2000, 0x00)
    ChrSetDirection(0x000F, 180, 400)
    WaitForThreadExit(0x0101, 0x0000)
    WaitForThreadExit(0x0101, 0x0002)

    ChrTalk(
        0x000F,
        (
            '#0170211615V#230F──嗯，就是这样。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0170211616V呵呵，卢安的各位市民\n',
            '也一定很尽兴了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_1D6A',
    )

    ChrTalk(
        0x0106,
        (
            '#0050211617V#057F#2P切……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050211618V也就是说这只是一场\n',
            '单纯的恶作剧啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1DB5')

    def _loc_1D6A(): pass

    label('loc_1D6A')

    ChrTalk(
        0x0103,
        (
            '#0030211619V#022F#2P无聊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030211620V总之就是\n',
            '单纯的恶作剧罢了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1DB5(): pass

    label('loc_1DB5')

    ChrTalk(
        0x000F,
        (
            '#0170211621V#231F说成是恶作剧，这种说法太难听了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0170211622V这是奉献给沉醉于选举的市民们\n',
            '一点点休闲和娱乐而已……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0170211623V希望你们能这么认为。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010211624V#1007F#2P你、你的机关我已经明白了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010211625V#1005F但你为什么\n',
            '要这么做呢！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010211626V『噬身之蛇』……\n',
            '到底有什么企图！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0170211627V#230F呵呵……\n',
            '那就不是我应该说的了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0170211628V我协助此次计划的\n',
            '理由只有一个……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0170211629V就是想能和科洛蒂娅公主──\n',
            '见上一面。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060211630V#044F#2P啊……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0170211631V#231F在逮捕市长时，您所展现出的\n',
            '高尚美丽……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0170211632V为了将这样的美丽据为己有，\n',
            '所以我才会协助这次的计划。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0170211633V在那之后的几个月──\n',
            '我都在焦急地等待这个机会哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060211634V#043F#2P咦，这个，那个……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010211635V#1015F#2P……逮捕市长，\n',
            '指的是戴尔蒙市长的事件吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010211636V#1020F#2P为、为什么\n',
            '你会知道那个时候的事啊！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0170211637V#230F呵呵，事件的过程中，\n',
            '我都在暗地里观察着你们。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0170211638V比如说……用这样的方法。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_219C')
    def lambda_219C():
        CameraMove(-262290, 0, 88050, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_219C)

    @scena.Lambda('lambda_21B4')
    def lambda_21B4():
        CameraSetDistance(1700, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_21B4)

    Sleep(500)

    PlaySE(203, 0x00, 0x64)
    ChrSetDirection(0x000F, 360, 2000)
    ChrSetChipByIndex(0x000F, 12)
    ChrSetSubChip(0x000F, 0)
    ChrSetDirection(0x000F, 270, 2000)
    ChrSetDirection(0x000F, 180, 2000)
    Sleep(500)

    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0104, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x00F7, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0105, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1500)

    OP_AD('ED6_DT24/C_VIS170._CH', 0x0000, 0x0000, 0x000001F4)
    Sleep(1000)

    Sleep(2000)

    OP_AE(0x000001F4)
    Sleep(1000)

    ChrTalk(
        0x0105,
        (
            '#0060211639V#043F#2P莫非你就是那时\n',
            '戴尔蒙家的……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 1, 0x1001)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2341',
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
        100,
        0,
        (
            TXT(0x00, '【◇烛台失窃任务没有完成】\n'),
            TXT(0x01, '【◇烛台失窃任务完成了】\n'),
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
        (0x00000000, 'loc_2328'),
        (0x00000001, 'loc_2330'),
        (-1, 'loc_2338'),
    )

    def _loc_2328(): pass

    label('loc_2328')

    OP_28(0x0057, 0x03, 0x10)

    Jump('loc_2338')

    def _loc_2330(): pass

    label('loc_2330')

    OP_28(0x0057, 0x04, 0x10)

    Jump('loc_2338')

    def _loc_2338(): pass

    label('loc_2338')

    FadeIn(300, 0)

    def _loc_2341(): pass

    label('loc_2341')

    If(
        (
            (Expr.Eval, "OP_29(0x0057, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_2463',
    )

    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010211640V#1005F#2P难道说……！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010211641V那个时候从市长官邸\n',
            '偷了烛台的『怪盗B』也是你！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060211642V#044F#2P啊……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0170211643V#5P呵呵……\n',
            '终于注意到了？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0170211644V我以为你们只要看了放在旧校舍的那些卡片\n',
            '早就应该注意到了才对。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2463(): pass

    label('loc_2463')

    @scena.Lambda('lambda_2469')
    def lambda_2469():
        CameraMove(-262290, 0, 87050, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_2469)

    @scena.Lambda('lambda_2481')
    def lambda_2481():
        CameraSetDistance(1810, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2481)

    Sleep(500)

    PlaySE(203, 0x00, 0x64)
    ChrSetDirection(0x000F, 360, 2000)
    ChrSetChipByIndex(0x000F, 11)
    ChrSetSubChip(0x000F, 0)
    ChrSetDirection(0x000F, 270, 2000)
    ChrSetDirection(0x000F, 180, 2000)
    ChrSetSubChip(0x000F, 0)
    Sleep(500)

    ChrTalk(
        0x000F,
        (
            '#0170211645V#230F怪盗就是美的崇拜者。\n',
            '注定会被高尚的东西所吸引。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0170211646V公主，您用您的高尚之美\n',
            '偷走了我的心啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0170211647V竟然把怪盗的心盗走……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0170211648V#233F啊，这是多么甜美的屈辱！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0170211649V您打算要如何赎回\n',
            '这样的罪孽呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0105, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0105,
        (
            '#0060211650V#043F#2P那、那个……\n',
            '你这么说我也很为难。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00F7, 0x0104, 400)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_266A',
    )

    ChrTalk(
        0x0106,
        (
            '#0050211651V#552F#2P这种自我陶醉的语气……\n',
            '和你这家伙简直没有什么两样！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_26B1')

    def _loc_266A(): pass

    label('loc_266A')

    ChrTalk(
        0x0103,
        (
            '#0030211652V#027F#2P这种陶醉的语气……\n',
            '似乎和某个人简直一模一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_26B1(): pass

    label('loc_26B1')

    ChrTurnDirection(0x0104, 0x00F7, 400)

    ChrTalk(
        0x0104,
        (
            '#0040211653V#6P#034F真失礼啊……\n',
            '不要把我和他混为一谈。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010211654V#1002F#2P『噬身之蛇』。\n',
            '好像和我想象的有所不同……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(250)
    PlaySE(213, 0x00, 0x64)
    ChrSetChipByIndex(0x0101, 13)
    ChrSetSubChip(0x0101, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010211655V#1005F#2P不过，你居然对科洛丝有所企图，\n',
            '那就更不能不闻不问了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060211656V#542F#1P艾丝蒂尔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_2870',
    )

    ChrSetDirection(0x0106, 360, 400)
    ChrTurnDirection(0x0104, 0x000F, 400)
    Fade(250)
    PlaySE(213, 0x00, 0x64)
    ChrSetChipByIndex(0x0106, 15)
    ChrSetSubChip(0x0106, 0)
    OP_0D()

    ChrTalk(
        0x0106,
        (
            '#0050211657V#054F#2P按照协会规定，\n',
            '我以非法入侵等嫌疑拘捕你。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050211658V包括『福音』等等的详情\n',
            '都要请你如实招来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_290B')

    def _loc_2870(): pass

    label('loc_2870')

    ChrSetDirection(0x0103, 360, 400)
    ChrTurnDirection(0x0104, 0x000F, 400)
    Fade(250)
    PlaySE(213, 0x00, 0x64)
    ChrSetChipByIndex(0x0103, 14)
    ChrSetSubChip(0x0103, 0)
    OP_0D()

    ChrTalk(
        0x0103,
        (
            '#0030211659V#024F#2P按照协会规定\n',
            '我以非法侵入等嫌疑拘捕你。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030211660V包括『福音』等等的详情\n',
            '都要请你如实招来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_290B(): pass

    label('loc_290B')

    ChrTalk(
        0x000F,
        (
            '#0170211661V#231F受不了你们……\n',
            '真是一些不解风情的人啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0170211662V要我来教训你们也无妨，\n',
            '不过既然选了这个地方……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0170211663V就让『他』来对付你们吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_29DA',
    )

    ChrTalk(
        0x0106,
        (
            '#0050211664V#052F#2P什么……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2A02')

    def _loc_29DA(): pass

    label('loc_29DA')

    ChrTalk(
        0x0103,
        (
            '#0030211665V#023F#2P你说什么……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2A02(): pass

    label('loc_2A02')

    Fade(250)
    ChrSetFlags(0x000F, 0x0002)
    ChrSetChipByIndex(0x000F, 32)
    ChrSetSubChip(0x000F, 0)
    OP_0D()
    Sleep(500)

    @scena.Lambda('lambda_2A22')
    def lambda_2A22():
        CameraMove(-262290, 0, 88050, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_2A22)

    @scena.Lambda('lambda_2A3A')
    def lambda_2A3A():
        CameraSetDistance(1700, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2A3A)

    WaitForThreadExit(0x0101, 0x0000)
    OP_99(0x000F, 0x00, 0x02, 1000)
    PlaySE(188, 0x00, 0x64)
    OP_20(0x00000000)
    Sleep(500)

    Fade(1000)
    CameraMove(-256350, 0, 81990, 0)
    OP_67(0, 6840, -10000, 0)
    CameraSetDistance(3480, 0)
    OP_6C(90000, 0)
    OP_6E(326, 0)
    OP_0D()
    PlaySE(133, 0x00, 0x64)

    @scena.Lambda('lambda_2AAF')
    def lambda_2AAF():
        OP_7C(0, 100, 300, 100)
        Yield()

        Jump('lambda_2AAF')

    DispatchAsync2(0x000F, 0x0003, lambda_2AAF)

    OP_0D()
    ChrClearFlags(0x0012, 0x0080)
    ChrSetFlags(0x0012, 0x0008)
    ChrSetFlags(0x0012, 0x0040)
    ChrSetFlags(0x0012, 0x0004)
    ChrSetPos(0x0012, -235000, 0, 82000, 270)
    OP_A1(0x0012, 0x0013)
    OP_CA(0x13, 0x02, 0x00000000)
    ChrSetFlags(0x0012, 0x0001)

    ExecExpressionWithValue(
        0x0012,
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
        0x0012,
        0x07,
        (
            (Expr.PushLong, 0x1770),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MapClearFlags(0x00000040)
    OP_7E(-500, -2000, 0, 80, 0)
    Sleep(500)

    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    @scena.Lambda('lambda_2B55')
    def lambda_2B55():
        ChrSetDirection(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2B55)

    @scena.Lambda('lambda_2B63')
    def lambda_2B63():
        ChrSetDirection(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_2B63)

    @scena.Lambda('lambda_2B71')
    def lambda_2B71():
        ChrSetDirection(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_2B71)

    @scena.Lambda('lambda_2B7F')
    def lambda_2B7F():
        ChrSetDirection(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x0104, 0x0001, lambda_2B7F)

    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010211666V#1020F#5P什、什么……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040211667V#032F#2P唔……\n',
            '我有一种不好～的预感。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_DB()
    OP_6F(0x0014, 0)
    OP_70(0x0014, 240)
    PlaySE(108, 0x00, 0x64)
    OP_73(0x0014)
    OP_72(0x0014, 0x0008)
    OP_72(0x0014, 0x0020)
    TerminateThread(0x000F, 0x03)
    OP_23(0x0085)
    PlaySE(200, 0x00, 0x64)
    OP_7C(100, 0, 5000, 1000)
    Sleep(1000)

    PlayBGM(41)
    Sleep(1000)

    CreateThread(0x0012, 0x00, 0x01, 0x0005)
    Sleep(3000)

    CreateThread(0x0012, 0x03, 0x01, 0x0004)
    Sleep(1200)

    TerminateThread(0x0012, 0x00)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Fade(1000)
    OP_B0(0x0013, 0x08)
    PlaySE(236, 0x00, 0x64)
    OP_6F(0x0013, 21)
    OP_70(0x0013, 40)
    Sleep(1500)

    PlaySE(200, 0x00, 0x64)
    OP_7C(100, 0, 5000, 1000)
    OP_73(0x0013)
    Sleep(1000)

    OP_71(0x0013, 0x0020)
    OP_B0(0x0013, 0x08)
    OP_6F(0x0013, 1)
    OP_70(0x0013, 16)
    Fade(500)
    CameraMove(-261589, 0, 84500, 0)
    OP_67(0, 6810, -10000, 0)
    CameraSetDistance(1860, 0)
    OP_6C(56000, 0)
    OP_6E(513, 0)
    OP_0D()
    OP_DC()

    ChrTalk(
        0x0101,
        (
            '#0010211668V#1020F#5P那、那是什么！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060211669V#042F#6P盔甲人马兵！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(250)
    ChrClearFlags(0x000F, 0x0002)
    ChrSetChipByIndex(0x000F, 11)
    ChrSetSubChip(0x000F, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x000F,
        (
            '#0170211670V#231F#5P呵呵，看来『他』好像是\n',
            '这个遗迹的守护者。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0170211671V本来已经处于在半坏状况了……\n',
            '不过，已经被我好心地修复好了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0170211672V反正机会难得，\n',
            '就让『他』来试一下你们的身手吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010211673V#1005F#5P开、开什么玩笑！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_2E84',
    )

    ChrTalk(
        0x0106,
        (
            '#0050211674V#054F#4P……来了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2EA8')

    def _loc_2E84(): pass

    label('loc_2E84')

    ChrTalk(
        0x0103,
        (
            '#0030211675V#024F#4P……来了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2EA8(): pass

    label('loc_2EA8')

    Sleep(500)

    Fade(500)
    TerminateThread(0x0012, 0x00)
    OP_72(0x0013, 0x0020)
    OP_0D()

    @scena.Lambda('lambda_2EC2')
    def lambda_2EC2():
        CameraMove(-258000, 0, 85500, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_2EC2)

    @scena.Lambda('lambda_2EDA')
    def lambda_2EDA():
        CameraSetDistance(1960, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2EDA)

    OP_6F(0x0013, 81)
    OP_70(0x0013, 97)
    PlaySE(236, 0x00, 0x64)
    OP_73(0x0013)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    TerminateThread(0x0101, 0xFF)
    Battle(0x0000044C, 0x00000000, 0x00, 0x0000, 0xFF)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000001, 'loc_2F20'),
        (-1, 'loc_2F25'),
    )

    def _loc_2F20(): pass

    label('loc_2F20')

    OP_B4(0x00)

    Jump('loc_2F25')

    def _loc_2F25(): pass

    label('loc_2F25')

    Return()

# id: 0x0003 offset: 0x2F26
@scena.Code('func_03_2F26')
def func_03_2F26():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    Sleep(500)

    MapClearFlags(0x00000001)
    OP_6F(0x0013, 160)
    ChrSetFlags(0x0012, 0x0080)
    ChrSetPos(0x0012, -256500, 0, 81800, 236)
    OP_A1(0x0012, 0x0013)
    OP_CA(0x13, 0x02, 0x00000000)
    OP_6F(0x0014, 240)
    ChrSetPos(0x0101, -263320, 0, 84630, 90)
    ChrSetPos(0x0105, -264530, 0, 82930, 90)
    ChrSetPos(0x00F7, -261260, 0, 83690, 90)
    ChrSetPos(0x0104, -262340, 0, 82220, 90)
    ChrClearFlags(0x000F, 0x0080)
    ChrSetPos(0x000F, -262320, 150, 91670, 180)
    ChrSetFlags(0x000F, 0x0004)
    ChrSetFlags(0x000F, 0x0001)
    ChrSetFlags(0x000F, 0x0040)
    CameraMove(-259000, 0, 84070, 0)
    OP_67(0, 6810, -10000, 0)
    CameraSetDistance(1810, 0)
    OP_6C(45000, 0)
    OP_6E(513, 0)
    FadeIn(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010211676V#1025F#5P赢、赢了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_311F',
    )

    ChrTalk(
        0x0106,
        (
            '#0050211677V#053F#5P呼……\n',
            '真不好对付。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_3082')
    def lambda_3082():
        CameraMove(-261290, 0, 88550, 1200)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_3082)

    @scena.Lambda('lambda_309A')
    def lambda_309A():
        OP_67(0, 6500, -10000, 1200)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_309A)

    ChrTurnDirection(0x0106, 0x000F, 400)
    ChrTurnDirection(0x0101, 0x000F, 400)
    ChrTurnDirection(0x0105, 0x000F, 400)
    ChrTurnDirection(0x00F7, 0x000F, 400)
    ChrTurnDirection(0x0104, 0x000F, 400)
    WaitForThreadExit(0x0101, 0x0000)
    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x0106,
        (
            '#0050211678V#054F#2P接下来就轮到你这家伙了……\n',
            '做好准备了吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3208')

    def _loc_311F(): pass

    label('loc_311F')

    ChrTalk(
        0x0103,
        (
            '#0030211679V#026F#5P呼……\n',
            '真不好对付。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_3152')
    def lambda_3152():
        CameraMove(-261290, 0, 88550, 1200)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_3152)

    @scena.Lambda('lambda_316A')
    def lambda_316A():
        OP_67(0, 6500, -10000, 1200)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_316A)

    ChrTurnDirection(0x0103, 0x000F, 400)
    ChrTurnDirection(0x0101, 0x000F, 400)
    ChrTurnDirection(0x0105, 0x000F, 400)
    ChrTurnDirection(0x00F7, 0x000F, 400)
    ChrTurnDirection(0x0104, 0x000F, 400)
    WaitForThreadExit(0x0101, 0x0000)
    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x0103,
        (
            '#0030211680V#022F#2P那么……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030211681V既然都到这个地步了，\n',
            '看来，应该是有所觉悟了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3208(): pass

    label('loc_3208')

    ChrTalk(
        0x000F,
        (
            '#0170211682V#230F#5P受不了你们……\n',
            '战斗的方式一点也没有优雅的感觉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(250)
    PlaySE(213, 0x00, 0x64)
    ChrSetChipByIndex(0x000F, 24)
    ChrSetSubChip(0x000F, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x000F,
        (
            '#0170211683V#231F#5P没办法了……\n',
            '我来示范给你们看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    OP_99(0x000F, 0x00, 0x05, 2500)

    ChrTalk(
        0x000F,
        (
            '#0170211684V#234F#5PＦｌａｍｍｅ！（火焰啊）！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_32EE')
    def lambda_32EE():
        CameraMove(-257000, 0, 86750, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_32EE)

    @scena.Lambda('lambda_3306')
    def lambda_3306():
        OP_67(0, 3910, -10000, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3306)

    @scena.Lambda('lambda_331E')
    def lambda_331E():
        CameraSetDistance(2410, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_331E)

    WaitForThreadExit(0x0101, 0x0000)
    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x0101, 0x0002)
    PlaySE(134, 0x00, 0x64)
    Sleep(200)

    Fade(500)
    LoadEffect(0x01, 'map\\\\mpfire5.eff')
    PlayEffect(0x01, 0x01, 0x00FF, -256000, 2900, 86750, 0, 0, 0, 1500, 1500, 1500, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0x02, 0x00FF, -256000, 2900, 77000, 0, 0, 0, 1500, 1500, 1500, 0x00FF, 0, 0, 0, 0)
    OP_C4(0x00, 0x00000002)
    OP_7E(-700, -280, -320, 150, 2000)
    ChrSetDirection(0x0101, 71, 400)
    ChrSetDirection(0x0105, 71, 400)
    ChrSetDirection(0x00F7, 71, 400)
    ChrSetDirection(0x0104, 71, 400)

    ChrTalk(
        0x0101,
        (
            '#0010211685V#1004F#5P什么……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060211686V#044F#5P篝火的火苗……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_344A')
    def lambda_344A():
        CameraMove(-261290, 0, 88550, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_344A)

    @scena.Lambda('lambda_3462')
    def lambda_3462():
        OP_67(0, 6500, -10000, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3462)

    @scena.Lambda('lambda_347A')
    def lambda_347A():
        CameraSetDistance(1810, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_347A)

    ChrSetSubChip(0x000F, 0)
    ChrTurnDirection(0x0101, 0x000F, 400)
    ChrTurnDirection(0x0105, 0x000F, 400)
    ChrTurnDirection(0x00F7, 0x000F, 400)
    ChrTurnDirection(0x0104, 0x000F, 400)
    WaitForThreadExit(0x0101, 0x0000)
    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x0101, 0x0002)

    ChrTalk(
        0x000F,
        (
            '#0170211687V#234F#5PＡｉｇｕｉｌｌｅ！（针啊）！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(250)
    ChrSetChipByIndex(0x000F, 26)
    ChrSetSubChip(0x000F, 6)
    OP_0D()
    ChrSetAfterImage(0x00, 0x000F, 0x0032, 0x01F4)

    @scena.Lambda('lambda_3508')
    def lambda_3508():
        CameraMove(-262290, 0, 87550, 800)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_3508)

    PlaySE(163, 0x00, 0x64)

    @scena.Lambda('lambda_3525')
    def lambda_3525():
        ChrJumpTo(0x00FE, -266170, 0, 88690, 500, 6000)

        ExitThread()

    DispatchAsync(0x000F, 0x0000, lambda_3525)

    CreateThread(0x0015, 0x00, 0x01, 0x0007)
    Sleep(100)

    CreateThread(0x0016, 0x00, 0x01, 0x0008)
    Sleep(100)

    CreateThread(0x0017, 0x00, 0x01, 0x0009)
    Sleep(100)

    CreateThread(0x0018, 0x00, 0x01, 0x000A)
    WaitForThreadExit(0x000F, 0x0000)
    WaitForThreadExit(0x000F, 0x0001)
    ChrSetAfterImage(0x01, 0x000F, 0x0000, 0x0000)

    @scena.Lambda('lambda_3580')
    def lambda_3580():
        OP_9E(0x00FE, 15, 0, 300, 4000)
        Yield()

        Jump('lambda_3580')

    DispatchAsync2(0x0101, 0x0001, lambda_3580)

    @scena.Lambda('lambda_359D')
    def lambda_359D():
        OP_9E(0x00FE, 15, 0, 300, 4000)
        Yield()

        Jump('lambda_359D')

    DispatchAsync2(0x00F7, 0x0001, lambda_359D)

    @scena.Lambda('lambda_35BA')
    def lambda_35BA():
        OP_9E(0x00FE, 15, 0, 300, 4000)
        Yield()

        Jump('lambda_35BA')

    DispatchAsync2(0x0105, 0x0001, lambda_35BA)

    @scena.Lambda('lambda_35D7')
    def lambda_35D7():
        OP_9E(0x00FE, 15, 0, 300, 4000)
        Yield()

        Jump('lambda_35D7')

    DispatchAsync2(0x0104, 0x0001, lambda_35D7)

    ChrTalk(
        0x0101,
        (
            '#0010211688V#1020F#2P啊……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060211689V#043F#2P呀……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040211690V#033F#2P啊……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_3696',
    )

    ChrTalk(
        0x0106,
        (
            '#0050211691V#055F#2P这是……\n',
            '『影缝』吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_36C7')

    def _loc_3696(): pass

    label('loc_3696')

    ChrTalk(
        0x0103,
        (
            '#0030211692V#523F#2P莫非……\n',
            '是『影缝』！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_36C7(): pass

    label('loc_36C7')

    TerminateThread(0x0101, 0x01)
    TerminateThread(0x00F7, 0x01)
    TerminateThread(0x0105, 0x01)
    TerminateThread(0x0104, 0x01)
    ChrSetSubChip(0x000F, 7)
    Sleep(75)

    ChrSetSubChip(0x000F, 0)
    Sleep(75)

    ChrSetChipByIndex(0x000F, 26)
    ChrSetSubChip(0x000F, 0)
    Sleep(500)

    ChrTalk(
        0x000F,
        (
            '#0170211693V#231F#5P呵呵，动不了了吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0170211694V你们对戴尔蒙市长的\n',
            '『宝杖』好像很吃惊吧……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0170211695V这种程度的技巧对我们执行者来说\n',
            '根本不需要依靠什么古代遗物来实现。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010211696V#1020F#2P怎、怎么会……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_3816',
    )

    ChrTalk(
        0x0106,
        (
            '#0050211697V#057F#2P可恶……\n',
            '太小看他了吗……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3842')

    def _loc_3816(): pass

    label('loc_3816')

    ChrTalk(
        0x0103,
        (
            '#0030211698V#522F#2P可恶，太大意了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3842(): pass

    label('loc_3842')

    ChrClearFlags(0x0013, 0x0080)
    ChrSetFlags(0x0013, 0x0040)
    PlaySE(407, 0x00, 0x64)
    OP_62(0x000F, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(800)

    @scena.Lambda('lambda_3873')
    def lambda_3873():
        CameraMove(-262370, 0, 81630, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_3873)

    @scena.Lambda('lambda_388B')
    def lambda_388B():
        OP_67(0, 7590, -10000, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_388B)

    WaitForThreadExit(0x0101, 0x0002)
    WaitForThreadExit(0x0101, 0x0003)
    ChrSetPos(0x0013, -263400, 4000, 69400, 0)
    CreateThread(0x0013, 0x01, 0x01, 0x000D)
    PlaySE(140, 0x00, 0x64)

    @scena.Lambda('lambda_38CA')
    def lambda_38CA():
        CameraMove(-262000, 0, 87800, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_38CA)

    @scena.Lambda('lambda_38E2')
    def lambda_38E2():
        OP_67(0, 7590, -10000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_38E2)

    @scena.Lambda('lambda_38FA')
    def lambda_38FA():
        ChrWalkTo(0x00FE, -264850, 300, 88290, 18000, 0x00)

        ExitThread()

    DispatchAsync(0x0013, 0x0002, lambda_38FA)

    Sleep(500)

    Sleep(300)

    ChrSetDirection(0x000F, 270, 0)
    ChrSetSubChip(0x000F, 6)
    ChrSetAfterImage(0x00, 0x000F, 0x0032, 0x01F4)
    PlaySE(163, 0x00, 0x64)

    @scena.Lambda('lambda_3938')
    def lambda_3938():
        ChrJumpTo(0x000F, -262510, 0, 89100, 500, 6000)

        ExitThread()

    DispatchAsync(0x000F, 0x0000, lambda_3938)

    Sleep(200)

    CreateThread(0x0019, 0x00, 0x01, 0x000B)
    WaitForThreadExit(0x000F, 0x0000)
    WaitForThreadExit(0x000F, 0x0001)
    ChrSetAfterImage(0x01, 0x000F, 0x0000, 0x0000)
    WaitForThreadExit(0x0013, 0x0002)
    ChrSetChipByIndex(0x0013, 20)
    ChrSetSubChip(0x0013, 0)
    TerminateThread(0x0013, 0x01)

    @scena.Lambda('lambda_3987')
    def lambda_3987():
        OP_9E(0x00FE, 15, 0, 300, 4000)
        Yield()

        Jump('lambda_3987')

    DispatchAsync2(0x0013, 0x0001, lambda_3987)

    WaitForThreadExit(0x0019, 0x0001)

    ChrTalk(
        0x0013,
        (
            '#0440211699V#310F#4P啾！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0013, 0x01)

    ChrTalk(
        0x0105,
        (
            '#0060211700V#043F#2P基库！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x000F, 7)
    Sleep(75)

    ChrSetSubChip(0x000F, 0)
    Sleep(75)

    ChrSetChipByIndex(0x000F, 26)
    ChrSetSubChip(0x000F, 0)

    ChrTalk(
        0x000F,
        (
            '#0170211701V#231F#2P你出现了啊，小小的骑士。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0170211702V我要对你的骑士精神表示敬意，\n',
            '不过请你先不要动。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(500)
    ChrSetChipByIndex(0x000F, 11)
    ChrSetSubChip(0x000F, 0)
    OP_0D()
    ChrSetDirection(0x000F, 225, 400)

    @scena.Lambda('lambda_3A93')
    def lambda_3A93():
        ChrWalkTo(0x00FE, -265000, 0, 84880, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_3A93)

    Sleep(300)

    @scena.Lambda('lambda_3AB3')
    def lambda_3AB3():
        CameraMove(-262900, 0, 84380, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_3AB3)

    @scena.Lambda('lambda_3ACB')
    def lambda_3ACB():
        OP_67(0, 6280, -10000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_3ACB)

    WaitForThreadExit(0x0101, 0x0000)
    WaitForThreadExit(0x0101, 0x0002)
    WaitForThreadExit(0x000F, 0x0001)
    ChrSetDirection(0x000F, 180, 400)

    ChrTalk(
        0x000F,
        (
            '#0170211703V#230F#1P科洛蒂娅公主。\n',
            '现在，您就是我的俘虏了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0170211704V呵呵，您的心情如何？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060211705V#047F#6P……请不要小看我。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060211706V#042F即便你能拘禁我的身躯，\n',
            '但也无法囚禁我的心……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060211707V只要我还活着，就一定不会屈服。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0170211708V#231F#1P对，就是这眼神！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0170211709V高尚、纯洁，\n',
            '绝不向任何人屈服的眼神！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0170211710V我要的就是这种充满希望的光芒！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010211711V#1005F#5P别、别在那里\n',
            '胡说八道了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_3CB1')
    def lambda_3CB1():
        OP_9E(0x00FE, 15, 0, 300, 4000)
        Yield()

        Jump('lambda_3CB1')

    DispatchAsync2(0x0101, 0x0001, lambda_3CB1)

    ChrTurnDirection(0x0101, 0x000F, 100)
    TerminateThread(0x0101, 0x01)

    ChrTalk(
        0x0101,
        (
            '#0010211712V#1005F#5P你这个戴着面具的古怪家伙！\n',
            '不许靠近科洛丝！',
            TxtCtl.Enter,
        ),
    )

    @scena.Lambda('lambda_3D1E')
    def lambda_3D1E():
        OP_9E(0x00FE, 15, 0, 300, 4000)
        Yield()

        Jump('lambda_3D1E')

    DispatchAsync2(0x00F7, 0x0001, lambda_3D1E)

    ChrTurnDirection(0x00F7, 0x000F, 100)
    TerminateThread(0x00F7, 0x01)

    @scena.Lambda('lambda_3D46')
    def lambda_3D46():
        OP_9E(0x00FE, 15, 0, 300, 4000)
        Yield()

        Jump('lambda_3D46')

    DispatchAsync2(0x0104, 0x0001, lambda_3D46)

    ChrSetDirection(0x0104, 323, 100)
    TerminateThread(0x0104, 0x01)
    CloseMessageWindow()
    ChrTurnDirection(0x000F, 0x0101, 400)

    ChrTalk(
        0x000F,
        (
            '#0170211713V#230F#3P真受不了你，\n',
            '竟然无法体会这面具的美……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0170211714V看来你还不了解\n',
            '什么才是真正的美。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040211715V#035F#2P呵呵……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000F, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrSetDirection(0x000F, 135, 400)

    ChrTalk(
        0x000F,
        (
            '#0170211716V#232F#1P嗯……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_3E4D')
    def lambda_3E4D():
        CameraMove(-262000, 0, 83690, 1500)

        ExitThread()

    DispatchAsync(0x000E, 0x0000, lambda_3E4D)

    @scena.Lambda('lambda_3E65')
    def lambda_3E65():
        OP_67(0, 6280, -10000, 1500)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_3E65)

    @scena.Lambda('lambda_3E7D')
    def lambda_3E7D():
        OP_6C(92000, 1500)

        ExitThread()

    DispatchAsync(0x000E, 0x0002, lambda_3E7D)

    WaitForThreadExit(0x000E, 0x0000)
    WaitForThreadExit(0x000E, 0x0001)
    WaitForThreadExit(0x000E, 0x0002)

    ChrTalk(
        0x0104,
        (
            '#0040211717V#031F#2P哈哈，看来我失礼了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040211718V#030F不，只是因为我发现你\n',
            '犯了一个太过低级错误。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040211719V所以才不知不觉地流露出\n',
            '没有恶意的微笑。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0170211720V#232F#5P哦？……有意思。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0170211721V你是说我\n',
            '想错问题了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040211722V#030F#2P的确，我从不吝惜去赞美\n',
            '公主殿下的美丽。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040211723V但这不是能够用你那小家子气的美学\n',
            '来加以衡量的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040211724V#035F回家温三年书再来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0170211725V#235F#5P啊，多么大言不惭！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0170211726V区区一个旅行演奏家，\n',
            '有什么资格来贬低我的美学！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0170211727V要是你回答不出来的话，看我怎么收拾你！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040211728V#035F#2P呵呵，那么我来问你──',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040211729V#030F何谓美？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0170211730V#231F#5P我还以为是什么呢，愚蠢的问题……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0170211731V美是高尚！\n',
            '是一种高高在上的光芒！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0170211732V除此以外\n',
            '还有什么样的答案？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040211733V#035F#2P呵呵，可笑……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(
        0x0104,
        (
            '#0040211734V#530F#2P#3S真正的美──那是爱！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()
    OP_62(0x000F, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x000F,
        (
            '#0170211735V#233F#5P……什么！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040211736V#035F#2P因为爱，人们才能感受美！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040211737V无爱之美不过是镜花水月！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040211738V#030F无论你是高贵还是卑微的人，\n',
            '只要有了爱，就都是美丽的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0170211739V#235F#5P哼，跟我耍小聪明……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0170211740V#234F但是在我看来，\n',
            '爱才是虚无的幻想！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0170211741V即便是不通过人的感悟，\n',
            '美本身仍然可以成立！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0170211742V比如，就像高山顶上盛开的鲜花，\n',
            '即便不为人所见，它也是美丽的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040211743V#032F#2P唔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    OP_62(0x00F7, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    OP_62(0x0105, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(1200)

    OP_63(0x0101)
    OP_63(0x00F7)
    OP_63(0x0105)

    ChrTalk(
        0x0101,
        (
            '#0010211744V#1019F#5P……那个。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_449F',
    )

    ChrTalk(
        0x0106,
        (
            '#0050211745V#551F#2P多么搞笑的对话啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_44CF')

    def _loc_449F(): pass

    label('loc_449F')

    ChrTalk(
        0x0103,
        (
            '#0030211746V#025F#2P唉，一下子紧张感就……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_44CF(): pass

    label('loc_44CF')

    ChrTalk(
        0x0105,
        (
            '#0060211747V#045F#4P真、真伤脑筋啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(
        0x000F,
        (
            '#0170211748V#230F#5P……想不到会在这种地方\n',
            '遇到同样在寻求美的劲敌。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0170211749V演奏家──你的名字叫什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040211750V#031F#2P奥利维尔·朗海姆。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040211751V为爱彷徨的\n',
            '漂泊诗人兼猎人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0170211752V#231F#5P呵呵……\n',
            '我会记住你的名字的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrClearFlags(0x000E, 0x0080)
    ChrSetPos(0x000E, -263660, 0, 73660, 339)
    OP_4A(0x000E, 255)
    LoadEffect(0x00, 'map\\\\mp032_00.eff')

    NpcTalk(
        0x000E,
        '女孩的声音',
        (
            '#0280211753V#1P啊～！\n',
            '小艾，总算找到你们了～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0104, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x00F7, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0105, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x000F, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTurnDirection(0x000F, 0x000E, 400)

    @scena.Lambda('lambda_46F9')
    def lambda_46F9():
        ChrWalkTo(0x00FE, -265030, 0, 80320, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_46F9)

    @scena.Lambda('lambda_4714')
    def lambda_4714():
        OP_6C(44000, 2000)

        ExitThread()

    DispatchAsync(0x000E, 0x0000, lambda_4714)

    @scena.Lambda('lambda_4724')
    def lambda_4724():
        CameraMove(-263200, 0, 82600, 2000)

        ExitThread()

    DispatchAsync(0x000E, 0x0002, lambda_4724)

    @scena.Lambda('lambda_473C')
    def lambda_473C():
        OP_67(0, 6280, -10000, 2000)

        ExitThread()

    DispatchAsync(0x000E, 0x0003, lambda_473C)

    WaitForThreadExit(0x000E, 0x0000)
    WaitForThreadExit(0x000E, 0x0001)
    WaitForThreadExit(0x000E, 0x0002)
    WaitForThreadExit(0x000E, 0x0003)

    ChrTalk(
        0x000E,
        (
            '#0280211754V#150F嘿嘿，实在是等不及了，\n',
            '所以我就过来看看了⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010211755V#1020F#5P朵、朵洛希！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060211756V#042F#5P不好！\n',
            '快跑！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0280211757V#154F咦……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000E, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x000E,
        (
            '#0280211758V#153F啊！\n',
            '带着面具的白色人影！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280211759V你就是幽灵吧～！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0170211760V#233F#5P不、不……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(250)
    ChrSetChipByIndex(0x000E, 25)
    ChrSetSubChip(0x000E, 0)
    OP_0D()

    ChrTalk(
        0x000E,
        (
            '#0280211761V#151F好，笑一个㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(124, 0x00, 0x64)
    PlayEffect(0x00, 0x00, 0x000E, 0, 1200, 500, 0, 0, 0, 500, 500, 500, 0x00FF, 0, 0, 0, 0)
    FadeOut(100, 16777215, -1)
    OP_0D()
    OP_C4(0x01, 0x00000002)
    OP_7E(-700, -1100, 100, 150, 0)
    TerminateThread(0x0101, 0x01)
    TerminateThread(0x00F7, 0x01)
    TerminateThread(0x0105, 0x01)
    TerminateThread(0x0104, 0x01)
    TerminateThread(0x0013, 0x01)
    StopEffect(0x01, 0x00)
    StopEffect(0x02, 0x00)
    FadeIn(200, 16777215)

    ChrTalk(
        0x000F,
        (
            '#0170211762V#235F#5P啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetChipByIndex(0x000E, 10)
    ChrSetSubChip(0x000E, 0)
    ChrSetFlags(0x0013, 0x0040)
    CreateThread(0x0013, 0x01, 0x01, 0x000D)
    PlaySE(140, 0x00, 0x64)

    ChrTalk(
        0x0013,
        (
            '#0440211763V#311F#3P啾⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CreateThread(0x0013, 0x01, 0x01, 0x000F)
    ChrSetDirection(0x0101, 315, 400)
    Sleep(300)

    ChrSetDirection(0x0101, 180, 400)

    ChrTalk(
        0x0101,
        (
            '#0010211764V#1004F#5P啊……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060211765V#542F#6P麻痹解除了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00F7, 0x000E, 400)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_4A5A',
    )

    ChrTalk(
        0x0106,
        (
            '#0050211766V#051F#5P原来如此……\n',
            '影子因为闪光灯消失了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4A97')

    def _loc_4A5A(): pass

    label('loc_4A5A')

    ChrTalk(
        0x0103,
        (
            '#0030211767V#021F#5P原来如此……\n',
            '影子因为闪光灯消失了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4A97(): pass

    label('loc_4A97')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_4AA6',
    )

    ChrSetChipByIndex(0x0106, 15)

    Jump('loc_4AAB')

    def _loc_4AA6(): pass

    label('loc_4AA6')

    ChrSetChipByIndex(0x0103, 14)

    def _loc_4AAB(): pass

    label('loc_4AAB')

    ChrSetChipByIndex(0x0104, 16)
    OP_0D()
    WaitForThreadExit(0x0101, 0x0002)
    ChrTurnDirection(0x0104, 0x000E, 400)

    ChrTalk(
        0x0104,
        (
            '#0040211768V#031F#2P哟，真是个不得了的女孩啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000E, 0x0104, 400)

    ChrTalk(
        0x000E,
        (
            '#0280211769V#151F#6P嗯，交给我你就放心吧～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280211770V虽然我也不知道\n',
            '自己到底是哪里厉害～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x0013, 0x0001)

    ChrTalk(
        0x000F,
        (
            '#0170211771V#231F哼哼哼……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0170211772V哈哈哈哈哈哈哈！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_4BA3')
    def lambda_4BA3():
        CameraMove(-262490, 0, 88500, 1200)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_4BA3)

    @scena.Lambda('lambda_4BBB')
    def lambda_4BBB():
        OP_67(0, 6810, -10000, 1200)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_4BBB)

    ChrSetAfterImage(0x00, 0x000F, 0x0032, 0x01F4)
    PlaySE(163, 0x00, 0x64)
    ChrJumpTo(0x000F, -263000, 150, 90400, 500, 5000)
    ChrSetAfterImage(0x01, 0x000F, 0x0000, 0x0000)

    @scena.Lambda('lambda_4BFF')
    def lambda_4BFF():
        ChrTurnDirection(0x0101, 0x000F, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_4BFF)

    @scena.Lambda('lambda_4C0D')
    def lambda_4C0D():
        ChrTurnDirection(0x00F7, 0x000F, 400)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_4C0D)

    @scena.Lambda('lambda_4C1B')
    def lambda_4C1B():
        ChrTurnDirection(0x0104, 0x000F, 400)

        ExitThread()

    DispatchAsync(0x0104, 0x0001, lambda_4C1B)

    @scena.Lambda('lambda_4C29')
    def lambda_4C29():
        ChrTurnDirection(0x000E, 0x000F, 400)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_4C29)

    @scena.Lambda('lambda_4C37')
    def lambda_4C37():
        ChrTurnDirection(0x0105, 0x000F, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_4C37)

    WaitForThreadExit(0x0101, 0x0002)
    ChrSetDirection(0x000F, 225, 400)

    @scena.Lambda('lambda_4C51')
    def lambda_4C51():
        ChrMoveTo(0x000F, -262460, 150, 91720, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_4C51)

    WaitForThreadExit(0x000F, 0x0001)
    ChrSetDirection(0x000F, 270, 400)
    PlaySE(130, 0x00, 0x64)
    OP_71(0x0015, 0x0004)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010211773V#1005F#2P啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060211774V#043F#2P他把『福音』！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrClearFlags(0x0105, 0x0020)
    ChrSetDirection(0x000F, 180, 400)

    ChrTalk(
        0x000F,
        (
            '#0170211775V#231F#6P好久没有过得\n',
            '这么开心了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0170211776V让我向你们致敬，诸位。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_4D6C',
    )

    ChrTalk(
        0x0106,
        (
            '#0050211777V#057F#2P你这家伙……\n',
            '还打算做什么吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4D9F')

    def _loc_4D6C(): pass

    label('loc_4D6C')

    ChrTalk(
        0x0103,
        (
            '#0030211778V#022F#2P你……\n',
            '还打算做什么吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4D9F(): pass

    label('loc_4D9F')

    ChrTalk(
        0x000F,
        (
            '#0170211779V#230F#6P呵呵……\n',
            '今晚就到此为止吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0170211780V不过对于诸位，\n',
            '我似乎有必要重新认识一下。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0170211781V不愧为是有资格和\n',
            '『漆黑之牙』并肩作战的人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010211782V#1020F#2P『漆黑之牙』……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060211783V#043F#2P莫非……\n',
            '是指约修亚！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0170211784V#231F#6P呵呵，我和他是旧交。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0170211785V我之所以会开始观察你们，\n',
            '就是因为看到他的身影。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0170211786V他好像已经恢复了所有的记忆……\n',
            '也不知他现在身在何处、在做些什么呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(250)
    ChrSetChipByIndex(0x000F, 24)
    ChrSetSubChip(0x000F, 0)
    OP_0D()
    OP_99(0x000F, 0x00, 0x05, 2500)
    LoadEffect(0x00, 'map\\\\mp046_00.eff')
    PlayEffect(0x00, 0x00, 0x000F, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlaySE(266, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010211787V#1020F#2P啊……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_503F',
    )

    ChrTalk(
        0x0106,
        (
            '#0050211788V#055F#2P什、什么……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5065')

    def _loc_503F(): pass

    label('loc_503F')

    ChrTalk(
        0x0103,
        (
            '#0030211789V#023F#2P莫非……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5065(): pass

    label('loc_5065')

    @scena.Lambda('lambda_506B')
    def lambda_506B():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 1000)

        ExitThread()

    DispatchAsync(0x000F, 0x0003, lambda_506B)

    Sleep(1500)

    StopEffect(0x00, 0x02)
    Sleep(300)

    OP_24(0x010A, 0x5A)
    Sleep(300)

    OP_24(0x010A, 0x50)
    Sleep(300)

    OP_24(0x010A, 0x46)
    Sleep(300)

    OP_24(0x010A, 0x3C)
    Sleep(300)

    OP_24(0x010A, 0x32)
    Sleep(300)

    OP_24(0x010A, 0x28)
    Sleep(300)

    OP_24(0x010A, 0x1E)
    Sleep(300)

    OP_23(0x010A)
    Sleep(600)

    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('布卢布兰的声音')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#0170211790V──再见了，诸位。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0170211791V计划才刚刚开始……\n',
            '尽量不要大意了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0170211792V我还打算以我自己的方式\n',
            '向你们发出挑战呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0170211793V呵呵，敬请期待吧。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    ChrSetFlags(0x000F, 0x0080)
    OP_20(0x00000BB8)
    Fade(250)
    ChrSetChipByIndex(0x0101, 65535)
    ChrSetChipByIndex(0x00F7, 65535)
    ChrSetChipByIndex(0x0105, 65535)
    ChrSetChipByIndex(0x0104, 65535)
    ChrSetSubChip(0x0101, 0)
    ChrSetSubChip(0x00F7, 0)
    ChrSetSubChip(0x0105, 0)
    ChrSetSubChip(0x0104, 0)
    ChrClearFlags(0x0013, 0x0080)
    ChrSetChipByIndex(0x0013, 20)
    ChrSetSubChip(0x0013, 0)
    CreateThread(0x0013, 0x01, 0x01, 0x000D)
    PlaySE(140, 0x00, 0x64)

    @scena.Lambda('lambda_51F5')
    def lambda_51F5():
        ChrMoveTo(0x0013, -263800, 1800, 82800, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0013, 0x0003, lambda_51F5)

    OP_0D()
    Sleep(500)

    CreateThread(0x0101, 0x01, 0x01, 0x0010)
    Sleep(200)

    CreateThread(0x0013, 0x02, 0x01, 0x000E)

    @scena.Lambda('lambda_5229')
    def lambda_5229():
        CameraMove(-262500, 150, 91000, 4000)

        ExitThread()

    DispatchAsync(0x000E, 0x0002, lambda_5229)

    @scena.Lambda('lambda_5241')
    def lambda_5241():
        OP_67(0, 6280, -10000, 4000)

        ExitThread()

    DispatchAsync(0x000E, 0x0003, lambda_5241)

    CreateThread(0x00F7, 0x01, 0x01, 0x0011)
    CreateThread(0x0105, 0x01, 0x01, 0x0012)
    Sleep(200)

    CreateThread(0x0104, 0x01, 0x01, 0x0013)
    Sleep(100)

    CreateThread(0x000E, 0x01, 0x01, 0x0014)
    WaitForThreadExit(0x000E, 0x0001)
    WaitForThreadExit(0x000E, 0x0002)
    WaitForThreadExit(0x000E, 0x0003)

    ChrTalk(
        0x0101,
        (
            '#0010211794V#1020F#5P消、消失了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060211795V#043F#6P难、难以置信……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0280211796V#153F哇～！\n',
            '好像变魔术一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040211797V#031F#6P哈哈哈。\n',
            '挺厉害的嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040211798V看来，我也只好承认\n',
            '他是我的劲敌了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0104, 400)

    ChrTalk(
        0x0101,
        (
            '#0010211799V#1005F#5P现在的问题不是这个！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010211800V撇开他那古怪的样子不说……\n',
            '那家伙可不是一般地强！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_5459',
    )

    ChrTalk(
        0x0106,
        (
            '#0050211801V#053F#2P是啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x00F7, 270, 400)
    ChrSetDirection(0x0105, 201, 400)

    ChrTalk(
        0x0106,
        (
            '#0050211802V#057F#2P『噬身之蛇』──\n',
            '比想象的更加难以对付。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_54CA')

    def _loc_5459(): pass

    label('loc_5459')

    ChrTalk(
        0x0103,
        (
            '#0030211803V#026F#2P是啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x00F7, 270, 400)
    ChrSetDirection(0x0105, 201, 400)

    ChrTalk(
        0x0103,
        (
            '#0030211804V#022F#2P『噬身之蛇』──\n',
            '比想象的更加难以对付。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_54CA(): pass

    label('loc_54CA')

    FadeOut(1500, 0, -1)
    OP_0D()
    Sleep(500)

    SetMessageWindowPos(72, 320, 56, 3)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '就这样……\n',
            '造成卢安各地骚动的幽灵事件落幕了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '隔天早晨，回到城里的艾丝蒂尔一行人\n',
            '和朵洛希暂时告别后，\n',
            '前往协会报告这次事件的经过。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(500)

    SetScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    NewScene('ED6_DT21/T2120._SN', 105, 0, 0)
    IdleLoop()

    Return()

# id: 0x0004 offset: 0x558D
@scena.Code('func_04_558D')
def func_04_558D():
    @scena.Lambda('lambda_5593')
    def lambda_5593():
        ChrJumpTo(0x00FE, -266600, 0, 81600, 300, 6000)

        ExitThread()

    DispatchAsync(0x0104, 0x0001, lambda_5593)

    Sleep(100)

    @scena.Lambda('lambda_55B6')
    def lambda_55B6():
        ChrJumpTo(0x00FE, -265890, 0, 83510, 300, 6000)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_55B6)

    Sleep(100)

    @scena.Lambda('lambda_55D9')
    def lambda_55D9():
        ChrJumpTo(0x00FE, -264550, 0, 81450, 300, 6000)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_55D9)

    Sleep(100)

    @scena.Lambda('lambda_55FC')
    def lambda_55FC():
        ChrJumpTo(0x00FE, -264380, 0, 82960, 300, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_55FC)

    ChrSetChipByIndex(0x0105, 17)
    ChrSetChipByIndex(0x0104, 16)
    ChrSetSubChip(0x0105, 0)
    ChrSetSubChip(0x0104, 0)

    Return()

# id: 0x0005 offset: 0x5629
@scena.Code('func_05_5629')
def func_05_5629():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_5682',
    )

    OP_24(0x00EC, 0x32)
    OP_B0(0x0013, 0x0D)
    OP_6F(0x0013, 251)
    OP_70(0x0013, 266)

    @scena.Lambda('lambda_564E')
    def lambda_564E():
        ChrMoveToRelativeAsync(0x00FE, -6000, 0, 0, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_564E)

    Sleep(500)

    PlaySE(236, 0x00, 0x64)
    Sleep(200)

    PlaySE(236, 0x00, 0x64)
    WaitForThreadExit(0x0012, 0x0001)
    OP_73(0x0013)

    Jump('func_05_5629')

    def _loc_5682(): pass

    label('loc_5682')

    Return()

# id: 0x0006 offset: 0x5683
@scena.Code('func_06_5683')
def func_06_5683():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_5696',
    )

    OP_6F(0x0014, 240)

    Jump('func_06_5683')

    def _loc_5696(): pass

    label('loc_5696')

    Return()

# id: 0x0007 offset: 0x5697
@scena.Code('func_07_5697')
def func_07_5697():
    ChrSetPos(0x0015, -264690, 500, 90200, 270)
    ChrClearFlags(0x0015, 0x0080)
    ChrSetFlags(0x0015, 0x0004)
    ChrSetSubChip(0x00FE, 0)
    PlaySE(503, 0x00, 0x64)

    @scena.Lambda('lambda_56C2')
    def lambda_56C2():
        ChrMoveTo(0x0015, -265090, -600, 83970, 20000, 0x00)

        ExitThread()

    DispatchAsync(0x0015, 0x0001, lambda_56C2)

    WaitForThreadExit(0x0015, 0x0001)
    ChrSetPos(0x0015, -265090, 0, 83870, 270)
    ChrSetSubChip(0x00FE, 2)

    Return()

# id: 0x0008 offset: 0x56F3
@scena.Code('func_08_56F3')
def func_08_56F3():
    ChrSetPos(0x0016, -264690, 500, 90200, 270)
    ChrClearFlags(0x0016, 0x0080)
    ChrSetFlags(0x0016, 0x0004)
    ChrSetSubChip(0x00FE, 0)
    PlaySE(503, 0x00, 0x64)

    @scena.Lambda('lambda_571E')
    def lambda_571E():
        ChrMoveTo(0x0016, -266090, -600, 82530, 20000, 0x00)

        ExitThread()

    DispatchAsync(0x0016, 0x0001, lambda_571E)

    WaitForThreadExit(0x0016, 0x0001)
    ChrSetPos(0x0016, -266090, 0, 82430, 270)
    ChrSetSubChip(0x00FE, 2)

    Return()

# id: 0x0009 offset: 0x574F
@scena.Code('func_09_574F')
def func_09_574F():
    ChrSetPos(0x0017, -264690, 500, 90200, 270)
    ChrClearFlags(0x0017, 0x0080)
    ChrSetFlags(0x0017, 0x0004)
    ChrSetSubChip(0x00FE, 0)
    PlaySE(503, 0x00, 0x64)

    @scena.Lambda('lambda_577A')
    def lambda_577A():
        ChrMoveTo(0x0017, -262500, -600, 83400, 20000, 0x00)

        ExitThread()

    DispatchAsync(0x0017, 0x0001, lambda_577A)

    WaitForThreadExit(0x0017, 0x0001)
    ChrSetPos(0x0017, -262500, 0, 83300, 270)
    ChrSetSubChip(0x00FE, 2)

    Return()

# id: 0x000A offset: 0x57AB
@scena.Code('func_0A_57AB')
def func_0A_57AB():
    ChrSetPos(0x0018, -264690, 500, 90200, 270)
    ChrClearFlags(0x0018, 0x0080)
    ChrSetFlags(0x0018, 0x0004)
    ChrSetSubChip(0x00FE, 0)
    PlaySE(503, 0x00, 0x64)

    @scena.Lambda('lambda_57D6')
    def lambda_57D6():
        ChrMoveTo(0x0018, -264000, -600, 81800, 20000, 0x00)

        ExitThread()

    DispatchAsync(0x0018, 0x0001, lambda_57D6)

    WaitForThreadExit(0x0018, 0x0001)
    ChrSetPos(0x0018, -264000, 0, 81700, 270)
    ChrSetSubChip(0x00FE, 2)

    Return()

# id: 0x000B offset: 0x5807
@scena.Code('func_0B_5807')
def func_0B_5807():
    ChrSetPos(0x0019, -263960, 500, 87940, 0)
    ChrClearFlags(0x0019, 0x0080)
    ChrSetFlags(0x0019, 0x0004)
    PlaySE(503, 0x00, 0x64)

    @scena.Lambda('lambda_582D')
    def lambda_582D():
        ChrMoveTo(0x0019, -267300, -600, 87000, 18000, 0x00)

        ExitThread()

    DispatchAsync(0x0019, 0x0001, lambda_582D)

    WaitForThreadExit(0x0019, 0x0001)
    ChrSetPos(0x0019, -267400, 0, 86950, 0)
    ChrSetSubChip(0x00FE, 1)

    Return()

# id: 0x000C offset: 0x585E
@scena.Code('func_0C_585E')
def func_0C_585E():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_5873',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('func_0C_585E')

    def _loc_5873(): pass

    label('loc_5873')

    Return()

# id: 0x000D offset: 0x5874
@scena.Code('func_0D_5874')
def func_0D_5874():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_5889',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('func_0D_5874')

    def _loc_5889(): pass

    label('loc_5889')

    Return()

# id: 0x000E offset: 0x588A
@scena.Code('func_0E_588A')
def func_0E_588A():
    ChrSetDirection(0x0013, 332, 400)
    OP_97(0x0013, -264500, 87900, -130000, 6000, 0x0001)
    ChrMoveTo(0x0013, -261700, 1800, 93300, 2000, 0x00)
    ChrSetChipByIndex(0x0013, 20)
    ChrSetSubChip(0x0013, 0)
    ChrSetDirection(0x0013, 270, 400)
    ChrMoveTo(0x0013, -261700, 1730, 93300, 1000, 0x00)
    TerminateThread(0x0013, 0x01)
    Sleep(250)

    ChrSetPos(0x0013, -261700, 1780, 93300, 270)
    ChrSetChipByIndex(0x0013, 29)
    ChrSetSubChip(0x0013, 0)
    OP_0D()

    Return()

# id: 0x000F offset: 0x5905
@scena.Code('func_0F_5905')
def func_0F_5905():
    ChrSetChipByIndex(0x0013, 19)
    ChrSetSubChip(0x0013, 0)
    ChrMoveTo(0x0013, -263000, 1100, 90400, 3000, 0x00)
    ChrSetDirection(0x0013, 263, 400)

    @scena.Lambda('lambda_5930')
    def lambda_5930():
        OP_97(0x0013, -264730, 86500, -250000, 7000, 0x0001)

        ExitThread()

    DispatchAsync(0x0013, 0x0003, lambda_5930)

    WaitForThreadExit(0x0013, 0x0003)
    ChrSetSubChip(0x0013, 0)
    ChrSetChipByIndex(0x0013, 20)
    ChrSetDirection(0x0013, 0, 400)
    ChrSetDirection(0x0105, 90, 400)
    ChrSetChipByIndex(0x0105, 21)
    ChrSetSubChip(0x0105, 2)
    ChrMoveTo(0x0013, -263700, 100, 83000, 2000, 0x00)
    Fade(500)
    TerminateThread(0x0013, 0x01)
    ChrSetFlags(0x0013, 0x0080)
    ChrSetChipByIndex(0x0105, 21)
    ChrSetSubChip(0x0105, 0)
    OP_0D()

    Return()

# id: 0x0010 offset: 0x599B
@scena.Code('func_10_599B')
def func_10_599B():
    ChrWalkTo(0x00FE, -263070, 0, 89810, 2000, 0x00)

    Return()

# id: 0x0011 offset: 0x59B0
@scena.Code('func_11_59B0')
def func_11_59B0():
    ChrWalkTo(0x00FE, -262410, 0, 88990, 2000, 0x00)

    Return()

# id: 0x0012 offset: 0x59C5
@scena.Code('func_12_59C5')
def func_12_59C5():
    ChrWalkTo(0x00FE, -264660, 0, 89430, 2000, 0x00)

    Return()

# id: 0x0013 offset: 0x59DA
@scena.Code('func_13_59DA')
def func_13_59DA():
    ChrWalkTo(0x00FE, -264290, 0, 87820, 2000, 0x00)

    Return()

# id: 0x0014 offset: 0x59EF
@scena.Code('func_14_59EF')
def func_14_59EF():
    ChrWalkTo(0x00FE, -263240, 0, 86990, 2000, 0x00)

    Return()

# id: 0x0015 offset: 0x5A04
@scena.Code('func_15_5A04')
def func_15_5A04():
    FadeOut(0, 0, -1)
    ClearScenaFlags(ScenaFlag(0x0240, 0, 0x1200))
    ClearScenaFlags(ScenaFlag(0x0240, 1, 0x1201))
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
        (0x00000000, 'loc_5A7E'),
        (0x00000001, 'loc_5A84'),
        (-1, 'loc_5A8A'),
    )

    def _loc_5A7E(): pass

    label('loc_5A7E')

    SetScenaFlags(ScenaFlag(0x0240, 0, 0x1200))

    Jump('loc_5A8A')

    def _loc_5A84(): pass

    label('loc_5A84')

    SetScenaFlags(ScenaFlag(0x0240, 1, 0x1201))

    Jump('loc_5A8A')

    def _loc_5A8A(): pass

    label('loc_5A8A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_5A98',
    )

    FormationAddMember(ChrTable['雪拉扎德'], 0xF7, 0xFF)

    Jump('loc_5A9C')

    def _loc_5A98(): pass

    label('loc_5A98')

    FormationAddMember(ChrTable['阿加特'], 0xF7, 0xFF)

    def _loc_5A9C(): pass

    label('loc_5A9C')

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
